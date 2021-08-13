 # Mini project 8- Converting Multiple image files to grayscale using multi-threading
 This project is used to convert multiple image files to grayscale using multi-threading. The file 'convert_multi_images_grayscale.py' is the main python file, 'command_line_solution.py' is the command line solution and the'results.png' and 'graph.png' are the results and graph images respectively.

# Dependencies to be installed

pip install matplotlib
pip install opencv-python

# Result Table

| Number of Threads | Time taken 
| ------------- |:-------------:| 
| 1     | 10.845
| 2   |  5.367
| 3 | 3.0677
| 4 | 2.7409
|5 | 2.4786
| 6     |2.2644
| 7   |  2.2961
| 8 |  2.3255
| 9| 2.2090
| 10 | 2.097
| 11     | 1.960
| 12   |  2.092
| 13 | 2.1163
| 14 | 2.0686
|15 | 2.1026
| 16     |2.1223
|17   |   2.0639
| 18 | 2.1091
| 19| 2.1381
| 20 | 2.1046



# Result Images



<img width="677" src="https://github.com/VatsalNanda/Mini-Projects-in-Python-ML-/blob/main/Mini_Proj_8-Convert%20multiple%20images%20to%20grayscale%20using%20multithreading/results.png">


<img width="677" src="https://github.com/VatsalNanda/Mini-Projects-in-Python-ML-/blob/main/Mini_Proj_8-Convert%20multiple%20images%20to%20grayscale%20using%20multithreading/graph.png">


Conclusion : The time taken for converting files to upper case first increases , then decreases by increasing threads. This is because at the beginning, parellism is achieved but later, the context switches time increasing due to frequent switching and time increases.


# Command Line Solution

Use

python <script>.py inputfile outputfile num_of_threads
  
  
