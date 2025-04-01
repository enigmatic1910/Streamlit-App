import streamlit as st

# Initialize task list
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Function to add a new task
def add_task(task, status):
    st.session_state.tasks.append({'task': task, 'status': status})

# Function to edit an existing task
def edit_task(index, new_task, new_status):
    st.session_state.tasks[index]['task'] = new_task
    st.session_state.tasks[index]['status'] = new_status

# Function to delete a task
def delete_task(index):
    st.session_state.tasks.pop(index)

# Streamlit layout
st.title("To-do App")

# Adding a task
with st.form(key='add_task_form'):
    new_task = st.text_input('Add Task')
    new_status = st.selectbox('Status', ['Not Started', 'In Progress', 'Completed'])
    add_task_button = st.form_submit_button('Add Task')
    if add_task_button and new_task:
        add_task(new_task, new_status)
        st.success(f'Task "{new_task}" added with status "{new_status}"!')

# Displaying tasks
if st.session_state.tasks:
    st.write("### Tasks List")
    for i, task in enumerate(st.session_state.tasks, start=1):
        st.write(f"{i}. {task['task']} - {task['status']}")

    # Selecting task number for edit and delete
    task_number = st.number_input('Task Number', min_value=1, max_value=len(st.session_state.tasks), step=1, key='task_number')

    # Editing a task
    with st.form(key='edit_task_form'):
        edit_task_input = st.text_input('Edit Task', key='edit_task_input')
        edit_status_input = st.selectbox('Edit Status', ['Not Started', 'In Progress', 'Completed'], key='edit_status_input')
        edit_button = st.form_submit_button('Edit Task')
        if edit_button and edit_task_input:
            edit_task(task_number - 1, edit_task_input, edit_status_input)
            st.success(f'Task {task_number} updated to "{edit_task_input}" with status "{edit_status_input}"')
            st.experimental_rerun()  # Rerun to immediately reflect changes

    # Deleting a task
    delete_button = st.button('Delete Task')
    if delete_button:
        delete_task(task_number - 1)
        st.success(f'Task {task_number} deleted')
        st.experimental_rerun()  # Rerun to immediately reflect changes
