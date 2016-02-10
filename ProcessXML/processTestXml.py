#!/usr/bin/env python
import xml.etree.ElementTree as ET
import sys

# Constants
kAttribAutoParam = "autoParam"

kActionRouteAddCoordinate = "addCoordinate"
kActionRouteOption = "addRouteOption"
kActionRouteMode = "calculateRoute"

kAutoParamRouteCoordinates = 'RouteCoordinates'
kAutoParamRouteOption = 'RouteOption'
kAutoParamRouteMode = 'RouteMode'


# Functions
def dblQuote(s1):
    return "\"%s\"" % s1


def processStep(element, level):
    """
    The auto-parameters will be set up here.  If the autoParam attribute is present in
    the action tag, then we'll go through the list of relevant parameters and randomly
    assign them to the value1 and/or value2 elements.

    These are the currently supported auto-parameters:
    - RouteCoordinates: Valid for Route.addCoordinate; Randomly assign long/lat for places 
                        in Berlin, Vancouver or Beijing
    - RouteOption: 	    Valid for Route.addRouteOption; Randomly allow/avoid routing 
                        options
    - RouteMode:		Valid for Route.calculateRoute; Randomly assign Drive or Walk 
                        routing
    """

    group = element.find('group').text
    actionElement = element.find('action')
    action = actionElement.text

    actionArgument = ""
    for value in element.iter('*'):
        if 'value' in value.tag:
            if value.text is not None:
                value.text = dblQuote(value.text)
                if value.tag == 'value1':
                    actionArgument += value.text
                else:
                    actionArgument = ", ".join((actionArgument, value.text))

    """
    value1 and value2 defaults to the values in the XML unless they are set
    to be auto parameters
    """

    value1 = element.find('value1').text
    value2 = element.find('value2').text

    """
    Calculate the indention needed depending on how many levels deep we are if we are Looping
    """
    indent = ""
    i = 0

    for i in range(0, level):
        indent = indent + "  "

    isAutoParam = False

    if (action == kActionRouteAddCoordinate):
        if ((len(actionElement.attrib) > 0) and (actionElement.attrib[kAttribAutoParam] == kAutoParamRouteCoordinates)):
            isAutoParam = True
            print indent + "  var Location = GenLocation();"

            value1 = "Location.latitude"
            value2 = "Location.longitude"

            print indent + "  %s.%s(%s, %s);" % (group, action, value1, value2)

    elif (action == kActionRouteOption):
        if ((len(actionElement.attrib) > 0) and (actionElement.attrib[kAttribAutoParam] == kAutoParamRouteOption)):
            isAutoParam = True

            value1 = "GenRouteOption()"
            value2 = "None"

            print indent + "  %s.%s(%s, \"%s\");" % (group, action, value1, value2)

    elif (action == kActionRouteMode):
        if ((len(actionElement.attrib) > 0) and (actionElement.attrib[kAttribAutoParam] == kAutoParamRouteMode)):
            isAutoParam = True

            value1 = "GenRouteMode()"
            value2 = "None"

            print indent + "  %s.%s(%s, \"%s\");" % (group, action, value1, value2)

    if (isAutoParam == False):
        print indent + "  %s.%s(%s);" % (group, action, actionArgument)


def processLoop(root, num_of_repeat, level):
    indent = "  "
    i = 0

    for i in range(0, level):
        indent = indent + "  "

    """
    Why the for loop indexes are being decorated (i.e., 'i%d') for each level is because
    JS only declares local variable at the function level and not block level.  This means
    that the same index within the inner loop of a nested FOR loop will have the side
    effect of altering the index of the outer loop.  Hence, we will decorate it with 
    the index thus giving it a distinct name.
    """

    print ""
    print "%sfor (var i%d = 0; i%d < %d; i%d++) {" % (indent, level, level, num_of_repeat, level)

    processRoot(root, level + 1)

    print "%s};\n" % indent


def processRoot(root, level):
    numRootElements = len(root)

    rootIndex = 0
    stepIndex = 0

    for rootIndex in range(0, numRootElements):
        if root[rootIndex].tag == 'step':
            processStep(root[rootIndex], level)
        elif root[rootIndex].tag == 'loop':
            num_of_repeat = int(root[rootIndex].attrib['repeat'])
            repeatNode = root[rootIndex]

            processLoop(repeatNode, num_of_repeat, level)


# Main
inputXml = sys.argv[1]

tree = ET.parse(inputXml)
root = tree.getroot()

print "function mainTest()"
print "{"

"""
Pass in both the root of the DOM tree and also a level so that we can get the 
indentation in the JS formatted properly in nested FOR loops (i.e., for the LOOP tags)
"""

processRoot(root, 1)

print "};"
