### GETTING ONLY THE TRUE NODE OF THE GLOBAL VARIABLES AND THEN ADDING IT TO THE FUNCTIONS

import graphviz
# working with the txt file
g = graphviz.Digraph("hbw-graph", graph_attr={"splines": "polyline", "nodesep": "1", "ranksep": "1"})

# input_str = """
# Function: TxtHighBayWarehouse::fsmStep()
# Global variable- reqVGRfetchContainer- 1
# Global variable- reqVGRfetch- 0
# Global variable- reqVGRcalib- 0
# Global variable- reqVGRresetStorage- 0
# if else block starting: fetchContainer() in TxtHighBayWarehouse::fsmStep()
# Function: TxtHighBayWarehouse::fetchContainer()
# Observers:
# if block starting: storage.fetchContainer() in TxtHighBayWarehouse::fetchContainer()
# Function: TxtHighBayWarehouseStorage::fetchContainer()
# Checking for Valid position
# if block starting: isValidPos() in TxtHighBayWarehouseStorage::fetchContainer()
# Function: TxtHighBayWarehouseStorage::isValidPos(StoragePos2 p)
# TxtHighBayWarehouseStorage::fetchContainer() - isValidPos() value: 0
# TxtHighBayWarehouse::fetchContainer() - storage.fetchContainer() value: 0
# Observers:
# storage.fetchContainer() returned false
# TxtHighBayWarehouse::fsmStep() - fetchContainer() value: 0
# """

input_str = open('hbw-graph.txt','r')

## this will go to the next line
# lines[lines.index(line)+1:]:

def parse_input(input_str):
    # lines = input_str.split("\n")
    calling = False
    i = 0
    function_call = None
    functions = []
    globals = []
    values = []
    false_block = None
    true_block = None
    for line in input_str:
      if i == 1000:
        break
      if "Global" in line:
        if line.split()[-1]=='1':
          print(line)
          global_var = line.replace(":","-").replace(":","-")
          g.node(global_var)
          globals.append(global_var)
          ## ADDING EDGE FROM FUNCTIONS TO GLOBAL VARIABLES
          if(len(functions) > 0):
            g.edge(functions[-1], globals[-1],  edge_attr={"len": "2.0"})
            i += 1
      elif "Function:" in line:
        # print(line)
        # name = line.split()[-1]
        function_name = line.split(": ")[1]
        # function_name = function_name.replace("(", "\\(").replace(")", "\\)").replace(":","-").replace(":","-")
        function_name = function_name.replace(":","-")
        g.node(function_name)
        #print("Function name: ",function_name)
        ## ADDING EDGE FROM GLOBAL VARIABLE TO FUNCTIONS
        if (len(globals) > 0):
          print(globals)
          for glo in globals:
            print(glo)
            g.edge(glo, function_name,  edge_attr={"len": "2.0"})
            i += 1
          globals = []
        ## ADDING EDGE FROM FUNCTIONS TO FUNCTIONS
        elif(len(functions) > 0) and calling:
          g.edge(str(functions[-1]), str(function_name))
          i += 1
          #g.edge(str(functions[-1]), str(function_name), edge_attr={"len": "2.0"})
          #if isinstance(functions[-1], str) and isinstance(function_name, str):
          #    g.edge(functions[-1], function_name, edge_attr={"len": "2.0"})

        functions.append(function_name)

      # elif "value" in line:
      elif "Calling" in line:
        calling = True
        print(line)
        value = line.replace("(", "\\(").replace(")", "\\)").replace(":","-").replace(":","-")
        g.node(value)
        if(len(values) > 0):
          g.edge(values[-1], value)
          i += 1
        else:
          g.edge(function_name, value)
          i += 1
        values.append(value)

parse_input(input_str)


g.render('hbw-graph.png')
with open('hbw-graph.png') as f:
    dot_graph = f.read()
graphviz.Source(dot_graph)
