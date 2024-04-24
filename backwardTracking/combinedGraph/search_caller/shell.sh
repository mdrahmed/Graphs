#!/bin/bash

# Define the file paths
important_files=(
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.4.Paper_Table_Format/Table_3/1.HBW_Retrieval/updated_idf_traces_0.005"
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.4.Paper_Table_Format/Table_3/2.HBW_Storage/updated_idf_traces_0.002"
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.4.Paper_Table_Format/Table_3/3.VGR-moving-wp-to-HBW/updated_idf_traces_0.0004"
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.4.Paper_Table_Format/Table_3/4.VGR-moving-wp-MPO/updated_idf_traces_0.0005"
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.4.Paper_Table_Format/Table_3/5.MPO_processing/updated_idf_traces_0.9"
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.4.Paper_Table_Format/Table_3/6.Delivering_WP_from_MPO_to_SLD/updated_idf_traces_0.3"
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.4.Paper_Table_Format/Table_3/7.Sorting_line/updated_idf_traces_0.3"
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.4.Paper_Table_Format/Table_3/8.Data_Theft_from_Camera/updated_idf_traces_0.001"
    #"/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.4.Paper_Table_Format/Table_3/9.Raw_Water_Processing_or_Overflow/updated_idf_traces_0.03"
    #"/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.4.Paper_Table_Format/Table_3/10.Chemical_Dosing/updated_idf_traces_0.1"
)
source_files=(
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/hbwall3"
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/hbwall3"
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/vgrall3"
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/vgrall3"
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/mpoall3"
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/mpoall3"
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.2.everything-logged-with-good/sldall3"
    "/home/raihan/CPS-VVI-LOGS-DATA/All-new-logs/10.3.attack-everything-logged-with-good/factory_main_cloud/main_cloud-v2"
    #""
)

# Loop through each file path pair and run the Python script
for i in $(seq 0 $((${#important_files[@]} - 1))); do
    #echo "Running search_caller.py for file pair $i:"
    #echo "Important file path: ${important_files[i]}"
    #echo "Source file path: ${source_files[i]}"
    python3 search_caller.py "${important_files[i]}" "${source_files[i]}"
done

