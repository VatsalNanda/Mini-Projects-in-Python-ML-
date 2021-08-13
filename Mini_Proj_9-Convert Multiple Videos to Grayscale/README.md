 # Mini project 9- Converting Multiple videos to grayscale using multi-threading
 This project is used to convert multiple image files to grayscale using multi-threading. The file 'convert_multiple_videos.py' is the main python file, 'command_line_solution.py' is the command line solution and 'graph.png'is the graph image respectively.

# Dependencies to be installed

pip install matplotlib
pip install opencv-python

# Result Table

| Number of Threads | Time taken 
| ------------- |:-------------:| 
| 5     | 13.6734
| 10   |  10.8765
| 15 | 11.8765
| 20 | 11.567



# Result Images


<img width="677" src="https://github.com/VatsalNanda/Mini-Projects-in-Python-ML-/blob/main/Mini_Proj_9-Convert%20Multiple%20Videos%20to%20Grayscale/graph.png">


Conclusion : The time taken for converting files to upper case first increases , then decreases by increasing threads. This is because at the beginning, parellism is achieved but later, the context switches time increasing due to frequent switching and time increases.


# Command Line Solution

Use

python <script>.py inputfile outputfile num_of_threads
  
  
