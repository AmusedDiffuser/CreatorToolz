# CreatorToolz

> [!NOTE]
> A collection of GUI (mostly) batch processing tools to optimize and simplify common tasks. I've made these to simplify and optimize content creation, with a focus on solving common problems when working with AI content creation tools.




## Batch_GitPuller.py

A non-GUI script that goes through each subfolder of the folder in which it is run, and preforms a git pull. Just to be sure it doesn't accidentaly break anything else, it cleverly checks to make sure it doesn't go more than one folder deep as it goes. Can be easily run with the command ```python Batch_Folder_GitPuller.py```



##  Batch_Text_AppendToStart-End_GUI_v4.py

GUI tool for batch processing a folder full of .txt files. I created this to simplify modifying training datasets, in case you think of a change after creating them. Offers seperate text input boxes for "insert before" and "insert after" existing text.



##  Batch_Text_Replacer_GUI_v2.py

GUI tool for batch "find-and-replace" processing of a folder full of .txt files. I created this to simplify changing trigger words, or fixing misspeled words.



##  Batch_MP3_EndTrimmer_GUI_v003.py

GUI tool for batch processing a folder full of .mp3 files. I created this to simplify trimming the end (outro, etc...) off of many mp3 files with a single click. Specify trim length in milliseconds (ie. input 1000 to trim 1 second).



##  Batch_Video_EndTrimmer_GUI_v1.py

GUI tool for batch processing a folder full of video files. Supports trimming .avi .mov and .mp4 files, though you can easily modify it to support other formats. I created this to simplify trimming the end (outro, company logo some video editing apps add, etc...) off of many video files with a single click. Specify trim length in milliseconds (ie. input 1000 to trim 1 second).



##  ListFileByTypeV9_GUI.py

GUI tool that creates a list of all files in a folder with a specified filetype and saves it to a .txt file. optional filter input will only include files containing specified strings. Optional checkboxes to: include file extension in output, scan subfolders, and include full path in output.

I'll add a requirements.txt file soon with an eplenation of how to use it...
