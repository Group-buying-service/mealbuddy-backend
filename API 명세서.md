# API 명세서  

- 모든 엔드포인트는 `https://mealbuddy.space/api` 를 기준으로 작성되어 있습니다.
- 응답이 따로 표기되지 않은 경우에는 status code와 에러시의 에러메세지만 반환됩니다.

## User
### 회원가입
- URL : `/user/register/`
- Method : `POST`
- Description : 유저를 새로 생성하고 토큰값을 생성하여 반환합니다.
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |email|string|필수|이메일|
    |username|string|필수|유저명|
    |password|string|필수|비밀번호|
    |password2|string|필수|비밀번호 확인|
    |address|string|필수|주소|


- Request 예시
    ```
    {
        "username": "testuser",
        "email": "test@email.com",
        "password": "test1234",
        "password2": "test1234",
        "address": "제주특별자치도 제주시 용담이동"
    }
    ```

- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |id|int|유저 pk|
    |email|string|이메일|
    |username|string|유저명|
    |address|string|주소|
    |token|string|토큰 값|
    
- Response 예시
    ```
    {
        "user": {
            "id": "1"
            "username": "testuser",
            "email": "test@email.com",
            "address": "제주특별자치도 제주시 용담이동",
            "token": "eefdf ... fdfQ"
        }
    }
    ```

### 로그인
- URL : `/user/login/`
- Method : `POST`
- Description : 로그인에 필요한 정보를 가지고 로그인합니다.
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |email|string|필수|이메일|
    |password|string|필수|비밀번호|

- Request 예시
    ```
    {
        "email": "test@email.com",
        "password": "test1234"
    }
    ```
- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |id|int|유저 pk|
    |email|string|이메일|
    |username|string|유저명|
    |address|string|주소|
    |token|string|토큰 값|
    
- Response 예시
    ```
    {
        "user": {
            "id": "1"
            "username": "testuser",
            "email": "test@email.com",
            "address": "제주특별자치도 제주시 용담이동",
            "token": "eefdf ... fdfQ"
        }
    }
    ```

### 유저 삭제
- URL : `/user/delete/`
- Method : `POST`
- Description : 유저의 정보를 삭제합니다.
 - Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|

- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |password|string|필수|비밀번호|

- Request 예시  
    ```
    {
        "password": "test1234"
    }
    ```


### 비밀번호 변경
- URL : `/user/changepassword/`
- Method : `POST`
- Description : 현재 비밀번호를 새로운 비밀번호로 변경합니다.
 - Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |current_password|string|필수|현재 비밀번호|
    |new_password1|string|필수|신규 비밀번호|
    |new_password2|string|필수|신규 비밀번호 확인|
- Request 예시  
    ```
    {
        "current_password": "test1234",
        "new_password1": "testtest",
        "new_password2": "testtest"
    }
    ```

### 유저 정보 확인
- URL : `/user/current/`
- Method : `GET`
- Description : 사용자의 정보를 확인합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|

- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |id|int|유저 pk|
    |email|string|이메일|
    |username|string|유저명|
    |address|string|주소|
    |token|string|토큰 값|
    
- Response 예시
    ```
    {
        "user": {
            "id": "1"
            "username": "testuser",
            "email": "test@email.com",
            "address": "제주특별자치도 제주시 용담이동",
            "token": "eefdf ... fdfQ"
        }
    }
    ```

### 프로필 업데이트
- URL : `/user/update/`
- Method : `POST`
- Description : 사용자의 username과 address를 변경합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |username|string||유저명|
    |address|string||주소|

- Request 예시  
    ```
    {
        "username": "test",
        "address": "경상남도 밀양시 내이동"
    }
    ```
- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |id|int|유저 pk|
    |email|string|이메일|
    |username|string|유저명|
    |address|string|주소|
    |token|string|토큰 값|
    
- Response 예시
    ```
    {
        "user": {
            "id": "1"
            "username": "testuser",
            "email": "test@email.com",
            "address": "제주특별자치도 제주시 용담이동",
            "token": "eefdf ... fdfQ"
        }
    }
    ```
---

## Post

### 파라미터 정의

- category
    - 족발,보쌈
    - 찜,탕,찌개
    - 돈까스,회,일식
    - 피자
    - 고기구이
    - 양식
    - 치킨
    - 중식
    - 아시안
    - 백반,죽,국수
    - 도시락
    - 분식
    - 카페,디저트
    - 페스트푸드

### 글 목록 조회
- URL : `/post/?category={category}&page={page}`
- Method : `GET`
- Description : 유저의 address와 일치하는 게시글 목록을 쿼리에 맞춰서 조회합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |cateogory|string||검색할 카테고리|
    |page|string||이동할 페이지|

- Request 예시  
    ```
    https://mealbuddy.space/api/post/?category=치킨&page=1
    ```

- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |posts|array|게시글 목록|
    |paginator|objects|페이지 정보|

    - posts  
        |파라미터|타입|설명|
        |---|---|---|
        |id|int|게시글 pk|
        |title|string|제목|
        |created_at|datetime|작성시간|
        |category|string|카테고리|
        |address|int|작성된 지역 주소|
        |content|string|내용|
        |is_compelete|boolean|모집완료 여부|
        |target_number|int|목표 인원수|
        |join_number|int|참여 인원수|
        |chat_id|int|게시글의 채팅방 pk|
        |writer|int|작성자 정보|

        - writer
            |파라미터|타입|설명|
            |---|---|---|
            |id|int|작성자 pk|
            |username|int|작성자 유저명|
            |email|int|작성자 이메일|
    
    - paginator
        |파라미터|타입|설명|
        |---|---|---|
        |page_range|array|페이지 범위, 현재페이지 기준으로 10개만 반환|
        |current_page|int|현재 페이지 번호|
        |prev_button|int, null|현재페이지-10, 1 미만일 경우 1, 1 페이지일 경우 null|
        |next_button|int, null|현재페이지+10, 마지막페이지보다 클경우 마지막페이지, 마지막페이지일 경우 null|
    
- Response 예시  
    ```
    {
        "posts" : [
            {
                "id": "1",
                "title": "치킨먹으실분 찾아요",
                "created_at": "2023-09-01 01:34:49.237071+00:00"
                "category": "치킨",
                "address": "제주특별자치도 제주시 용담이동",
                "content": "치킨이 너무 먹고싶네요",
                "is_compelete": "true",
                "target_number": "3",
                "join_number": "3",
                "chat_id": "1",
                "writer": {
                    "id": "3",
                    "username": "test",
                    "email": "test@test.com"
                }
            }
        ]
        "paginator": {
            "page_range": "[1,2,3,4,5,6,7,8,9,10]",
            "current_page": "1",
            "prev_button": "null",
            "next_button": "11",
        }
    }
    ```

### 글 작성
- URL : `/post/write/`
- Method : `POST`
- Description : 새로운 글을 작성합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |title|string|필수|제목|
    |category|string|필수|카테고리|
    |target_number|int|필수|목표 인원, 최소 2, 최대 10|
    |content|string|필수|내용|
- Request 예시  
    ```
    {
        "title": "치킨이 먹고싶어요",
        "category": "치킨",
        "모집인원": "8",
        "content": "치킨이 먹고싶어요",
    }
    ```

- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |id|int|게시글 pk|
    |title|string|제목|
    |created_at|datetime|작성시간|
    |category|string|카테고리|
    |address|int|작성된 지역 주소|
    |content|string|내용|
    |is_compelete|boolean|모집완료 여부|
    |target_number|int|목표 인원수|
    |join_number|int|참여 인원수|
    |chat_id|int|게시글의 채팅방 pk|
    |writer|int|작성자 정보|

    - writer
        |파라미터|타입|설명|
        |---|---|---|
        |id|int|작성자 pk|
        |username|int|작성자 유저명|
        |email|int|작성자 이메일|

- Response 예시  
    ```
    {
        "id": "1",
        "title": "치킨먹으실분 찾아요",
        "created_at": "2023-09-01 01:34:49.237071+00:00",
        "category": "치킨",
        "address": "제주특별자치도 제주시 용담이동",
        "content": "치킨이 너무 먹고싶네요",
        "is_compelete": "true",
        "target_number": "3",
        "join_number": "3",
        "chat_id": "1",
        "writer": {
            "id": "3",
            "username": "test",
            "email": "test@test.com"
        }
    }
    ```

### 글 상세 조회
- URL : `/post/detail/{id}/`
- Method : `GET`
- Description : 작성된 글의 상세 내용을 조회합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|게시글 pk|

- Request 예시  
    ```
    https://mealbuddy.space/api/post/detail/1/
    ```

- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |id|int|게시글 pk|
    |title|string|제목|
    |created_at|datetime|작성시간|
    |category|string|카테고리|
    |address|int|작성된 지역 주소|
    |content|string|내용|
    |is_compelete|boolean|모집완료 여부|
    |target_number|int|목표 인원수|
    |join_number|int|참여 인원수|
    |chat_id|int|게시글의 채팅방 pk|
    |is_joined|bool|요청을 보낸사람의 채팅 참여 여부|
    |writer|int|작성자 정보|

    - writer
        |파라미터|타입|설명|
        |---|---|---|
        |id|int|작성자 pk|
        |username|int|작성자 유저명|
        |email|int|작성자 이메일|

- Response 예시  
    ```
    {
        "id": "1",
        "title": "치킨먹으실분 찾아요",
        "created_at": "2023-09-01 01:34:49.237071+00:00",
        "category": "치킨",
        "address": "제주특별자치도 제주시 용담이동",
        "content": "치킨이 너무 먹고싶네요",
        "is_compelete": "true",
        "target_number": "3",
        "join_number": "3",
        "chat_id": "1",
        "is_joined": "true",
        "writer": {
            "id": "3",
            "username": "test",
            "email": "test@test.com"
        }
    }
    ```

### 글 수정
- URL : `/post/detail/{id}/edit/`
- Method : `POST`
- Description : 작성되어 있는 글을 수정합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|게시글 pk|
    |title|string|필수|제목|
    |category|string|필수|카테고리|
    |target_number|int|필수|목표 인원, 최소 2, 최대 10|
    |content|string|필수|내용|

- Request 예시  
    ```
    https://mealbuddy.space/api/post/detail/1/

    {
        "title": "치킨이 먹고싶어요",
        "category": "치킨",
        "모집인원": "8",
        "content": "치킨이 먹고싶어요",
    }
    ```

- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |id|int|게시글 pk|
    |title|string|제목|
    |created_at|datetime|작성시간|
    |category|string|카테고리|
    |address|int|작성된 지역 주소|
    |content|string|내용|
    |is_compelete|boolean|모집완료 여부|
    |target_number|int|목표 인원수|
    |join_number|int|참여 인원수|
    |chat_id|int|게시글의 채팅방 pk|
    |is_joined|bool|요청을 보낸사람의 채팅 참여 여부|
    |writer|int|작성자 정보|

    - writer
        |파라미터|타입|설명|
        |---|---|---|
        |id|int|작성자 pk|
        |username|int|작성자 유저명|
        |email|int|작성자 이메일|

- Response 예시  
    ```
    {
        "id": "1",
        "title": "치킨먹으실분 찾아요",
        "created_at": "2023-09-01 01:34:49.237071+00:00",
        "category": "치킨",
        "address": "제주특별자치도 제주시 용담이동",
        "content": "치킨이 너무 먹고싶네요",
        "is_compelete": "true",
        "target_number": "3",
        "join_number": "3",
        "chat_id": "1",
        "is_joined": "true",
        "writer": {
            "id": "3",
            "username": "test",
            "email": "test@test.com"
        }
    }
    ```

### 글 삭제
- URL : `/post/detail/{id}/delete/`
- Method : `POST`
- Description : 작성되어 있는 글을 삭제합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
    |X-CSRFToken|string|필수|csrftoken|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|게시글 pk|
- Request 예시  
    ```
    https://mealbuddy.space/post/detail/1/delete/
    ```

---

## Chat

- 소켓 통신의 경우 엔드포인트를 따로 기재합니다.

### 채팅방 정보 조회
- URL : `/chat/{id}/`
- Method : `GET`
- Description : 채팅방의 정보 및 메세지를 조회합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|채팅방 pk|
- Request 예시  
    ```
    https://mealbuddy.space/chat/1/
    ```
- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |messages|array|메세지 목록|
    |title|string|채팅방 제목|
    |target_number|int|채팅방 최대 인원|
    |join_number|int|채팅방 참여 인원|
    |writer|objects|채팅방 생성자 정보|

    - messages  
        |파라미터|타입|설명|
        |---|---|---|
        |message|array|내용|
        |created_at|datetime|작성시간|
        |chatroom|int|채팅방 pk|
        |user|objects|작성유저|
        - user  
            |파라미터|타입|설명|
            |---|---|---|
            |id|int|작성자 pk|
            |username|string|작성자 유저명|
            |email|string|작성자 이메일|
    
    - writer  
        |파라미터|타입|설명|
        |---|---|---|
        |id|array|채팅방 생성자 pk|
        |username|array|채팅방 생성자 유저명|
        |email|array|채팅방 생성자 이메일|

- Response 예시  

    ```
    {
        "messages": [
            {
                "message": "안녕하세요",
                "created_at": "2023-09-01 01:34:49.237071+00:00",
                "chatroom": "1",
                "user": {
                    "id": "1",
                    "username": "test",
                    "email": "test@test.com"
                }
            },
            {
                "message": "안녕하세요!!",
                "created_at": "2023-09-01 01:55:49.237071+00:00",
                "chatroom": "1",
                "user": {
                    "id": "2",
                    "username": "test2",
                    "email": "test2@test.com"
                }
            }
        ],
        "writer": {
            "id": "1",
            "username": "test",
            "email": "test@test.com"
        }
    }
    ```

### 채팅방 접근 권한 얻기
- URL : `/chat/{id}/`
- Method : `POST`
- Description : 채팅방의 접근 권한을 얻습니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|채팅방 pk|
- Request 예시  
    ```
    https://mealbuddy.space/chat/1/
    ```
- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |messages|array|메세지 목록|
    |title|string|채팅방 제목|
    |target_number|int|채팅방 최대 인원|
    |join_number|int|채팅방 참여 인원|
    |writer|objects|채팅방 생성자 정보|

    - messages  
        |파라미터|타입|설명|
        |---|---|---|
        |message|array|내용|
        |created_at|datetime|작성시간|
        |chatroom|int|채팅방 pk|
        |user|objects|작성유저|
        - user  
            |파라미터|타입|설명|
            |---|---|---|
            |id|int|작성자 pk|
            |username|string|작성자 유저명|
            |email|string|작성자 이메일|
    
    - writer  
        |파라미터|타입|설명|
        |---|---|---|
        |id|array|채팅방 생성자 pk|
        |username|array|채팅방 생성자 유저명|
        |email|array|채팅방 생성자 이메일|

- Response 예시  

    ```
    {
        "messages": [
            {
                "message": "안녕하세요",
                "created_at": "2023-09-01 01:34:49.237071+00:00",
                "chatroom": "1",
                "user": {
                    "id": "1",
                    "username": "test",
                    "email": "test@test.com"
                }
            },
            {
                "message": "안녕하세요!!",
                "created_at": "2023-09-01 01:55:49.237071+00:00",
                "chatroom": "1",
                "user": {
                    "id": "2",
                    "username": "test2",
                    "email": "test2@test.com"
                }
            }
        ],
        "writer": {
            "id": "1",
            "username": "test",
            "email": "test@test.com"
        }
    }
    ```

### 채팅방 유저 리스트 조회
- URL : `/chat/{id}/user/`
- Method : `GET`
- Description : 채팅방의 접근 권한을 얻습니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|채팅방 pk|
- Request 예시  
    ```
    https://mealbuddy.space/chat/1/
    ```
- Response Elements

    |파라미터|타입|설명|
    |---|---|---|
    |response|array|유저리스트|
    |id|int|작성자 pk|
    |username|string|작성자 유저명|
    |email|string|작성자 이메일|

- Response 예시  

    ```
    {
        0: [
            {
                "id": "1",
                "username": "test",
                "email": "test@test.com"
            },
            {
                "id": "2",
                "username": "test2",
                "email": "test2@test.com"
            }
        ]
    }
    ```

### 채팅방 나가기
- URL : `/chat/{id}/user/`
- Method : `DELETE`
- Description : 채팅방의 접근권한을 삭제합니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|채팅방 pk|
- Request 예시  
    ```
    https://mealbuddy.space/chat/1/
    ```

### 채팅방 유저 강퇴
- URL : `/chat/{id}/user/ban/`
- Method : `POST`
- Description : 채팅방에 있는 유저를 강퇴합니다. blacklist에 등록되어서 같은 채팅방에 다시 참여할 수 없습니다.
- Request Header  

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |Authorization|string|필수|token(공백한칸)value 양식|
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|채팅방 pk|
    |target_user_id|int|필수|강퇴할 유저 pk|

- Request 예시
    ```
    https://mealbuddy.space/api/post/detail/1/

    {
        "target_user_id": "1"
    }
    ```

## 채팅방 웹소켓 통신

- URL: `wss://mealbuddy.com/ws/chat/{id}/?token={token}`
- Method: `WEB SOCKET`
- Description: 웹 소켓 방식으로 신규 메세지를 주고받습니다.
- Request Elements

    |파라미터|타입|필수여부|설명|
    |---|---|---|---|
    |id|int|필수|채팅방 pk|
    |token|string|필수|엑세스 토큰|

- Request 예시

    ```
    wss://mealbuddy.com/ws/chat/1/?token=eYDfefd...EDfke
    ```

- Response  
    WebSocket Event 형태로 응답.


### 웹소켓 메세지 송수신
- Event: `onMessage`
- type: `chat.message`, `chat.user.join`, `chat.user.leave`
- Request Elements
    |파라미터|타입|설명|
    |---|---|---|
    |message|string|내용|

- Request 예시
    ```
        {
            "message": "안녕하세요!"
        }
    ```

- Event Elements

    |파라미터|타입|설명|
    |---|---|---|
    |type|string|이벤트 타입|
    |message|objects|신규 메세지|

    - messages  
        |파라미터|타입|설명|
        |---|---|---|
        |message|array|내용|
        |created_at|datetime|작성시간|
        |chatroom|int|채팅방 pk|
        |user|objects, null|작성유저|
        - user  
            |파라미터|타입|설명|
            |---|---|---|
            |id|int|작성자 pk|
            |username|string|작성자 유저명|
            |email|string|작성자 이메일|
- Event 예시

    ```
    {
        "type": "chat.message"
        "message": "안녕하세요!!",
        "created_at": "2023-09-01 01:55:49.237071+00:00",
        "chatroom": "1",
        "user": {
            "id": "2",
            "username": "test2",
            "email": "test2@test.com"
        }
    }
    ```


### 웹 소켓 종료
- Event: `onClose`
- Event Elements

    |파라미터|타입|설명|
    |---|---|---|
    |code|int|종료코드. 4040 일 경우 채팅방이 삭제되었음을 의미|
