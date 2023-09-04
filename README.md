# 밀버디🍚
 - 다양한 사용자들이 음식 주문을 결합하여 배달비를 절감하고, 주문 과정을 더 효율적으로 만드는 웹사이트 개발.
 - 사용자는 개인 정보를 등록하고 로그인하여 서비스를 이용.
 - 게시글 확인 및 채팅 참여기능을 통해 소통.
 - 메뉴 추천기능과 날씨정보를 통한 메뉴 선정에 도움.


## 📖 프로젝트 소개 및 계획이유
 - 프로젝트 소개    
> - 다양한 사용자들이 음식 주문을 결합하여 배달비를 절감하고, 주문 과정을 더 효율적으로 만드는 웹사이트 개발.   
> - 사용자는 개인 정보를 등록하고 로그인하여 서비스를 이용.   
> - 게시글 확인 및 채팅 참여기능을 통해 소통.   
> - 메뉴 추천기능과 날씨정보를 통한 메뉴 선정에 도움.   
 - 프로젝트 계획이유
> 높아져 가는 배달비로 인해 배달을 시키는데에 부담이 발생하고,    
최소금액이 존재하여 내가 먹을 양보다 많은 양을 시키게 되고 그로 인해 원하지 않은 많은 음식물 쓰레기와 지출이 발생합니다.   
또한, 알뜰 배달이라는 서비스가 존재하지만 긴 배달시간으로 인해 음식이 식거나 형태가 변형되는 경우가 발생하여 이와 같은 문제로 인해 느끼는 불편함을 해소하고자 계획하였습니다.   


## 🕰 개발 기간
> 2023.08.17 ~ 2023.09.04

## 🤝 멤버 구성
- 김바름 - django channels를 이용한 채팅기능 구현, open API 연동, 프론트엔드 구현, docker-compose를 통한 배포
- 김범석 - JWT를 이용해 로그인, 회원가입 기능 구현, API 명세서 작성, README 작성
- 류형환 - 게시글 CRUD 구현, 주소와 카테고리 별 필터기능 구현
- 임동성 - USER 관련 정보 수정 기능 구현, 다음 주소 API 연동

## 📕 배포 주소
- https://mealbuddy.space/

- 테스트 계정
```
Email : test@test.com
Password : password123
```

## ⚙ 기술 스택
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=PostgreSQL&logoColor=white"> <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=Redis&logoColor=white"> <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=React&logoColor=white"> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white"> <img src="https://img.shields.io/badge/Daphne-5b9bd5?style=for-the-badge&logo=Daphne&logoColor=white"> <img src="https://img.shields.io/badge/gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white"> <img src="https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=Nginx&logoColor=white">


## 📌 주요 기능 
 - 메뉴 추천
 - 지역기반 배달 공동구매 중개
 - 주민간의 채팅 서비스
 - 지역 날씨 정보 확인

## 🚩 API 명세서


## 🚩 API 경로
**백엔드**  
|URL|기능|
|---|---|
|`/user/login/`|로그인|
|`/user/logout/`|로그아웃|
|`/user/signup/`|회원가입|
|`/user/delete/`|회원탈퇴|
|`/user/password/change/`|비밀번호 변경|
|`/user/profile/`|프로필 확인 및 수정|
|`/token/refresh/`|JWT 토큰 갱신|
|`/chat/list/`|게시글 목록 및 검색|
|`/chat/list/self/`|자신의 게시글 목록|
|`/chat/detail/<chat_id>/`|채팅페이지|
|`/chat/<chat_id>/update/`|채팅 제목 수정 및 추가질문|
|`/chat/write/`|채팅 페이지 작성|
|`/chat/delete/<chat_id>`|채팅 삭제|
|`/chat/<chat_id>/comment/write/`|댓글 작성|
|`/chat/comment/delete/<comment_id>`|댓글 삭제|
|`/chat/comment/delete/child/<childcomment_id>`|대댓글 삭제(댓글과 같은 뷰)|
|`/chat/comment/update/<comment_id>`|댓글 수정|
|`/chat/comment/update/child/<childcomment_id>`|대댓글 수정(댓글과 같은 뷰)|

## 🛢데이터베이스 설계
<img src="db설계도.png">

## 🖥 화면 구성
|   **회원가입**  |
|:---------------:|
|<img src="/gif/회원가입(정보입력).gif">|
|   **회원가입(오류처리)**  |
|<img src="/gif/회원가입(오류처리).gif">|
|   **로그인**   |
|<img src="/gif/로그인.gif">|
|   **음식추천 및 날씨정비**   |
|<img src="/gif/음식추천및날씨정보.gif">|
|   **회원정보 수정**   |
|<img src="/gif/회원정보_수정.gif">|
|   **회원탈퇴**   |
|<img src="/gif/회원탈퇴.gif">|
|   **글 작성**   |
|<img src="/gif/글-작성.gif">|
|   **글 수정**   |
|<img src="/gif/글-수정.gif">|
|   **모집상태 변경 및 삭제**   |
|<img src="/gif/모집상태-변경-및-삭제.gif">|
|   **게시판**   |
|<img src="/gif/게시판.gif">|
|   **채팅**   |
|<img src="/gif/채팅.gif">|
## 🗜 아키텍쳐
### 디렉토리 구조
```
📦backend
├─ .gitignore
├─ README.md
├─ channels-redis.txt
├─ chat
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ consumers.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ routing.py
│  ├─ serializer.py
│  ├─ signal.py
│  ├─ templates
│  │  └─ chat
│  │     ├─ APIindex.html
│  │     ├─ APIroom.html
│  │     ├─ index.html
│  │     └─ room.html
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ core
│  ├─ exceptions.py
│  └─ models.py
├─ group_buying_service
│  ├─ API
│  │  ├─ openAI.py
│  │  └─ weather.py
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ utils
│  │  ├─ coordinate_convert.py
│  │  └─ paginator.py
│  ├─ views.py
│  └─ wsgi.py
├─ manage.py
├─ openAPI
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ templates
│  │  └─ openAPI
│  │     └─ index.html
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ post
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  ├─ 0001_initial.py
│  │  ├─ 0002_initial.py
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ signal.py
│  ├─ static
│  │  ├─ chat.css
│  │  ├─ common.css
│  │  ├─ list.css
│  │  ├─ login-join.css
│  │  ├─ next.png
│  │  ├─ prev.png
│  │  ├─ table.css
│  │  ├─ view.css
│  │  └─ write.css
│  ├─ templates
│  │  └─ post
│  │     ├─ form_error.html
│  │     ├─ post_detail.html
│  │     ├─ post_edit.html
│  │     ├─ post_form.html
│  │     └─ post_list.html
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ requirement.txt
├─ static
│  ├─ chat.css
│  ├─ common.css
│  ├─ list.css
│  ├─ login-join.css
│  ├─ next.png
│  ├─ prev.png
│  ├─ table.css
│  ├─ view.css
│  └─ write.css
├─ templates
│  ├─ base.html
│  └─ index.html
└─ user
   ├─ __init__.py
   ├─ admin.py
   ├─ api
   │  ├─ renderers.py
   │  ├─ serializers.py
   │  ├─ urls.py
   │  └─ views.py
   ├─ apps.py
   ├─ backends.py
   ├─ managers.py
   ├─ migrations
   │  ├─ 0001_initial.py
   │  └─ __init__.py
   ├─ models.py
   ├─ permissions.py
   ├─ templates
   │  ├─ profile.html
   │  ├─ register.html
   │  ├─ updatepassword.html
   │  └─ user_login.html
   └─ tests.py
```

## 💡 후기
- 김바름
> Channels를 이용한 web socket 통신이나, docker를 이용한 배포과정 등을 처음 경험해봐서, 배워나가면서 오류를 고쳐나가는 과정이 어려웠습니다.    
> 깃허브에서 브랜치전략을 이용하면서 머지과정에서 다양한 충돌을 다루는 방법을 알게되었고, channels나 docker에 대해서도 이해할 수 있는 기회였습니다.
- 김범석
> JWT를 이용해 토큰을 관리하는 것을 이해하는 것이 조금 어려웠었고, 팀프로젝트로 협업하는 것이 처음이라 서투르다보니 문제점이 많았었습니다.   
> 다른 팀원들에게 정말 많이 배웠고 제대로 팀프로젝트를 진행한 것이 처음이라서 새로운 경험을 할 수 있었습니다. 이를 통해 django drf와 git을 다루는 데에 익숙해져서 스스로가 조금 더 성장한 시간이었습니다.
- 류형환
> 프론트가 없는 상태에서 기능만 개발하다 보니 기능이 완성되어도 데이터가 정상적으로 주고받고 데이터 처리를 확인하는 작업이 어색하여 어려웠습니다.   
> drf가 무엇인지 조금이나마 아는 시간이 되었고 깃허브를 이용하여 팀과 협업을 한 경우가 이번이 처음이었는데 깃허브를 다루는 게 조금이나마 익숙해지는 시간이었던 거 같습니다.
- 임동성
> 로그인과정에서의 token개념에 대해서 이해가 어려웠었고 django에 대해서 익숙해 지기가 어려웠습니다.   
> 협업의 중요성에 대해서 깨닫게 되고 drf에서 사용되는 Serializer의 구조에 대해서 좀 더 직관적으로 알게되었습니다. 

