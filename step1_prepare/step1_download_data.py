import os
import pandas

# Read the storybooks CSV into a DataFrame, and write the DataFrame to a CSV file
videos_csv_url = 'https://raw.githubusercontent.com/elimu-ai/webapp-lfs/main/lang-ENG/videos.csv'
print(os.path.basename(__file__), f'videos_csv_url: {videos_csv_url}')
videos_dataframe = pandas.read_csv(videos_csv_url)
print(os.path.basename(__file__), f'videos_dataframe: \n{videos_dataframe}')
videos_dataframe.to_csv('step1_videos.csv', index=False)

# Read the students CSV into a DataFrame
students_csv_url = 'https://raw.githubusercontent.com/elimu-ai/ml-datasets/main/lang-ENG/students.csv'
print(os.path.basename(__file__), f'students_csv_url: {students_csv_url}')
students_dataframe = pandas.read_csv(students_csv_url)
print(os.path.basename(__file__), f'students_dataframe: \n{students_dataframe}')

# For each student, read the video learning events CSV into a DataFrame
all_events = []
for student_id in students_dataframe['id']:
    print(os.path.basename(__file__), f'\nstudent_id: {student_id}')
    video_learning_events_csv_url = f"https://raw.githubusercontent.com/elimu-ai/ml-datasets/main/lang-ENG/student-id-{student_id}/video-learning-events.csv"
    print(os.path.basename(__file__), f'video_learning_events_csv_url: {video_learning_events_csv_url}')
    video_learning_events_dataframe = pandas.read_csv(video_learning_events_csv_url)
    
    # Drop the `id` column since it it just an Android Room database ID which is not relevant here
    video_learning_events_dataframe = video_learning_events_dataframe.drop(columns=['id'])

    # Add the student ID as a column in the DataFrame since it is not already included
    video_learning_events_dataframe.insert(0, 'student_id', student_id)

    print(os.path.basename(__file__), f'video_learning_events_dataframe.size: {video_learning_events_dataframe.size}')
    if (video_learning_events_dataframe.size > 0):
        # Append the student's events to the dataframe containing _all_ events
        all_events.append(video_learning_events_dataframe)

# Combine multiple DataFrames into one
all_events_dataframe = pandas.concat(all_events, ignore_index=True)
print(os.path.basename(__file__), f'all_events_dataframe: \n{all_events_dataframe}')

# Write the DataFrame containing all events to a CSV file
all_events_dataframe.to_csv('step1_video_learning_events.csv', index=False)
