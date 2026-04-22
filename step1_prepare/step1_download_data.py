import os
import pandas

# Read the storybooks CSV into a DataFrame, and write the DataFrame to a CSV file
videos_csv_url = 'https://raw.githubusercontent.com/elimu-ai/webapp-lfs/main/lang-ENG/videos.csv'
print(os.path.basename(__file__), 'videos_csv_url: {}'.format(videos_csv_url))
videos_dataframe = pandas.read_csv(videos_csv_url)
print(os.path.basename(__file__), 'videos_dataframe: \n{}'.format(videos_dataframe))
videos_dataframe.to_csv('step1_videos.csv', index=False)

with open('step1_video_learning_events.csv', 'w') as f:
    pass
students_url = 'https://raw.githubusercontent.com/elimu-ai/ml-datasets/main/lang-ENG/students.csv'
print(os.path.basename(__file__), 'students_url: {}'.format(students_url))
students_dataframe = pandas.read_csv(students_url)
print(os.path.basename(__file__), 'students_dataframe: \n{}'.format(students_dataframe))
student_ids = students_dataframe['id'].copy()

if not student_ids.empty:
    video_learning_events_csv_url = f"https://raw.githubusercontent.com/elimu-ai/ml-datasets/main/lang-ENG/student-id-{student_ids[0]}/video-learning-events.csv"
    video_learning_events_dataframe = pandas.read_csv(video_learning_events_csv_url)
    video_learning_events_dataframe.to_csv('step1_video_learning_events.csv', index=False)
for student_id in student_ids[1:]:
    video_learning_events_csv_url = f"https://raw.githubusercontent.com/elimu-ai/ml-datasets/main/lang-ENG/student-id-{student_id}/video-learning-events.csv"
    print(f"URL: {video_learning_events_csv_url}")
    video_learning_events_dataframe = pandas.read_csv(video_learning_events_csv_url)
    print(os.path.basename(__file__), 'video_learning_events_dataframe: \n{}'.format(video_learning_events_dataframe))
    video_learning_events_dataframe.to_csv('step1_video_learning_events.csv', mode='a', index=False, header=False)