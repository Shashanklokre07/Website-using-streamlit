import streamlit as st

# -------------------- CONFIG --------------------
VALID_USERNAME = "admin"
VALID_PASSWORD = "admin123"

# -------------------- LOGIN LOGIC --------------------
def login_page():
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid username or password")

def dashboard():
    st.success(f"Welcome, {st.session_state.username}")
    st.write("You are logged in.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

# -------------------- MAIN APP --------------------
def main():
    st.set_page_config(
        page_title="Login App",
        page_icon="🔐",
        layout="centered"
    )

    st.title("Secure Login")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        dashboard()
    else:
        login_page()

if __name__ == "__main__":
    main()
