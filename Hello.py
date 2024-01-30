# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#import streamlit as st
#from streamlit.logger import get_logger

#LOGGER = get_logger(__name__)


#def run():
#    st.set_page_config(
#        page_title="Hello",
#        page_icon="👋",
#    )

#    st.write("# Welcome to Streamlit! 👋")

#    st.sidebar.success("Select a demo above.")

#    st.markdown(
#        """
#        Streamlit is an open-source app framework built specifically for
#        Machine Learning and Data Science projects.
#        **👈 Select a demo from the sidebar** to see some examples
#        of what Streamlit can do!
#        ### Want to learn more?
#        - Check out [streamlit.io](https://streamlit.io)
#        - Jump into our [documentation](https://docs.streamlit.io)
#        - Ask a question in our [community
#          forums](https://discuss.streamlit.io)
#        ### See more complex demos
#        - Use a neural net to [analyze the Udacity Self-driving Car Image
#          Dataset](https://github.com/streamlit/demo-self-driving)
#        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
#    """
 #   )


#if __name__ == "__main__":
#    run()

import streamlit as st
from datetime import datetime

# Function to display chat messages
def display_messages(messages):
    for message in messages:
        st.text(f"{message['sender']} ({message['timestamp']}): {message['content']}")

# Function to add a new message
def add_message(messages, sender, content):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messages.append({'sender': sender, 'content': content, 'timestamp': timestamp})

# Main function
def main():
    st.title("User-to-User Chat")

    # Initialize messages list
    messages = []

    # Get user names
    user1 = st.text_input("Enter User 1's Name:", key='user1')
    user2 = st.text_input("Enter User 2's Name:", key='user2')

    # User 1 input
    user1_input = st.text_input(f"{user1}'s message:")
    if st.button(f"Send to {user2}", key='send_user1'):
        add_message(messages, user1, user1_input)

    # User 2 input
    user2_input = st.text_input(f"{user2}'s message:")
    if st.button(f"Send to {user1}", key='send_user2'):
        add_message(messages, user2, user2_input)

    # Display messages
    display_messages(messages)

if __name__ == "__main__":
    main()

