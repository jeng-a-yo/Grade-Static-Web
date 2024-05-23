import streamlit as st

# 預設用戶名和密碼（在真實應用中應使用更安全的方法存儲和管理用戶數據）
USER_CREDENTIALS = {'admin': 'password',
                    'jengyoyo': 'password',}

def login(username, password):
    if USER_CREDENTIALS.get(username) == password:
        st.session_state['logged_in'] = True
        st.session_state['username'] = username
        return True
    return False

def logout():
    st.session_state['logged_in'] = False
    st.session_state['username'] = None

def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        st.title('登入')
        username = st.text_input('用戶名')
        password = st.text_input('密碼', type='password')
        if st.button('登入'):
            if login(username, password):
                st.success('登入成功')
            else:
                st.error('用戶名或密碼錯誤')
    else:
        st.sidebar.title(f'歡迎, {st.session_state["username"]}')
        if st.sidebar.button('登出'):
            logout()
            st.sidebar.success('已登出')

        st.title('主頁')
        st.write('這是登入後才能看到的內容')

if __name__ == '__main__':
    main()
