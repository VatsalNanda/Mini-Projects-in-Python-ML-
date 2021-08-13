 # Mini project 7- Converting Multiple text files to uppercase using multi-threading
 This project is used to convert multiple text files to uppercase using multi-threading. The file 'converting_to_uppercase_using_multithreading.py' is the main python file, 'command_line.py' is the command line solution and the'results.png' and 'graphs.png' are the results and graph images respectively.

# Dependencies to be installed

pip install matplotlib

# Result Table

| Number of Threads | Time taken 
| ------------- |:-------------:| 
| 1     | 73.71825933456421
| 2   |  64.22967195510864
| 3 | 63.3087100982666
| 4 | 64.3447527885437
|5 | 63.21729040145874
| 6     |67.50598073005676
| 7   |  62.78048300743103
| 8 |  64.10699987411499
| 9| 65.74505805969238
| 10 | 67.17373490333557
| 11     | 67.13695693016052
| 12   |  68.32771682739258
| 13 | 68.09865617752075
| 14 | 70.9521131515503
|15 | 71.42451691627502
| 16     |71.04484295845032
|17   |   84.99924397468567
| 18 |  73.30099892616272
| 19| 73.30887413024902 
| 20 | 77.10597681999207



# Result Images



<img width="677" src="https://github.com/VatsalNanda/Mini-Projects-in-Python-ML-/blob/main/Mini_Proj_7-converting%20multiple%20text%20files%20to%20uppercase%20%20using%20multi-threading/graph.png">


Conclusion : The time taken for converting files to upper case first increases , then decreases by increasing threads. This is because at the beginning, parellism is achieved but later, the context switches time increasing due to frequent switching and time increases.



<img width="677" src="https://github.com/VatsalNanda/Mini-Projects-in-Python-ML-/blob/main/Mini_Proj_7-converting%20multiple%20text%20files%20to%20uppercase%20%20using%20multi-threading/results.png">

# Command Line Solution

Use

python <script>.py inputfile outputfile num_of_threads
  
  
