<!-- 
GET POST PUT PATCH DELETE

### 
- URL : 
- Method : 
- Description :
- Request  
    ```
    {
        
    }
    ```
- Response
    ```
    {
        
    }
    ```

 -->

# API 명세서
## User
### 회원가입
- URL : /user/register/
- Method : POST
- Description : 유저를 새로 생성하고 토큰값을 생성하여 반환합니다.
- Request  
    ```
    {
        "username": "testuser",
        "email": "test@email.com",
        "password": "test1234",
        "address": "제주 제주시 공항로 2 제주국제공항"
    }
    ```
    
- Response
    ```
    {
        "user": {
            "username": "testuser",
            "email": "test@email.com",
            "address": "제주 제주시 공항로 2 제주국제공항",
            "token": "token값"
        }
    }
    ```

### 로그인
- URL : /user/login/
- Method : POST
- Description : 로그인에 필요한 정보를 가지고 로그인합니다.
- Request  
    ```
    {
        "email": "test@email.com",
        "password": "test1234"
    }
    ```
- Response
    ```
    {
        "user": {
            "email": "test@email.com",
            "username": "testuser",
            "last_login": "2023-09-01 01:34:49.237071+00:00",
            "token": "token값"
        }
    }
    ```

### 로그아웃
- URL : /user/logout/
- Method : POST
- Description : 로그아웃을 합니다.
- Request  
    ```
    {
        
    }
    ```
- Response
    ```
    {
        
    }
    ```

### 유저 삭제
- URL : /user/delete/
- Method : DELETE
- Description : 유저의 정보를 삭제합니다.
- Request  
    ```
    {
        
    }
    ```
- Response
    ```
    {
        
    }
    ```

### 비밀번호 변경
- URL : /user/changepassword/
- Method : POST
- Description : 현재 비밀번호를 새로운 비밀번호로 변경합니다.
- Request  
    ```
    {
        
    }
    ```
- Response
    ```
    {
        
    }
    ```

### 프로필 업데이트
- URL : /user/update/
- Method : POST
- Description :
- Request  
    ```
    {
        
    }
    ```
- Response
    ```
    {
        
    }
    ```

---

## Blog
### 글 목록 조회
- URL : /blog/
- Method : GET
- Description : 작성한 글 목록을 조회합니다.
- Request  
    ```
    {
        
    }
    ```
- Response
    ```
    {
        
    }
    ```

### 글 작성
- URL : /blog/write/
- Method : POST
- Description : 새로운 글을 작성합니다.
- Request  
    ```
    {
        
    }
    ```
- Response
    ```
    {
        
    }
    ```

### 글 상세 조회
- URL : /blog/detail/{id}/
- Method : GET
- Description : 작성된 글의 상세 내용을 조회합니다.
- Request  
    ```
    {
        
    }
    ```
- Response
    ```
    {
        
    }
    ```

### 글 수정
- URL : /blog/detail/{id}/edit/
- Method : PATCH
- Description : 글을 수정합니다.
- Request  
    ```
    {
        
    }
    ```
- Response
    ```
    {
        
    }
    ```

### 글 삭제
- URL : /blog/detail/{id}/delete/
- Method : DELETE
- Description : 현재 작성되어 있는 글을 삭제합니다.
- Request  
    ```
    {
        
    }
    ```
- Response
    ```
    {
        
    }
    ```

---

## Chat
### 
- URL : 
- Method : 
- Description :
- Request  
    ```
    {
        
    }
    ```
- Response
    ```
    {
        
    }
    ```