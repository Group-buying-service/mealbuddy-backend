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
  > 최소금액이 존재하여 내가 먹을 양보다 많은 양을 시키게 되고 그로 인해 원하지 않은 많은 음식물 쓰레기와 지출이 발생합니다.  
  > 또한, 알뜰 배달이라는 서비스가 존재하지만 긴 배달시간으로 인해 음식이 식거나 형태가 변형되는 경우가 발생하여 이와 같은 문제로 인해 느끼는 불편함을 해소하고자 계획하였습니다.

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

[API 명세서](https://github.com/Group-buying-service/mealbuddy-backend/blob/main/API%20%EB%AA%85%EC%84%B8%EC%84%9C.md)

## 🚩 API 경로

**백엔드**  
- prefix: `/api`

|URL|기능|
|---|---|
|`/user/login/`|로그인|
|`/user/register/`|회원가입|
|`/user/delete/`|회원탈퇴|
|`/user/changepassword/`|비밀번호 변경|
|`/user/update/`|유저정보 수정|
|`/user/current/`|유저정보 확인|
|`/post/`|글 목록 조회|
|`/post/detail/<post_id>/`|글 상세 조회|
|`/post/write/`|글 작성|
|`/post/detail/<post_id>/edit/`|글 수정|
|`/post/detail/<post_id>/delete/`|글 삭제|
|`/chat/<room_id>/`|채팅방 상태 조회, 채팅방 접근권한 얻기, 채팅방 삭제|
|`/chat/<room_id>/user/`|채팅방 유저 조회, 채팅방 나가기|
|`/chat/<room_id>/user/ban/`|채팅방 유저 강퇴|
|`/openAPI/weather/`|날씨 정보 조회|
|`/openAPI/foodchoicer/`|음식 추천|

## 🛢데이터베이스 설계

<img src="db설계도.png">

## 🖥 화면 구성

|   **회원가입**  |
|:---------------:|
|<img src="/gif/회원가입_정보입력_.gif">|
|   **회원가입(오류처리)**  |
|<img src="/gif/회원가입_오류처리_.gif">|
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
📦mealbuddy-backend
│  .env
│  manage.py
│  README.md
│  requirements.txt
├─chat
│  │  admin.py
│  │  apps.py
│  │  consumers.py
│  │  models.py
│  │  routing.py
│  │  serializer.py
│  │  signal.py
│  │  urls.py
│  │  views.py
│  └─migrations
│     │  0001_initial.py
│     └  0002_initial.py    
├─core
│  │  exceptions.py
│  └─models.py        
├─group_buying_service
│  │  asgi.py
│  │  settings.py
│  │  urls.py
│  │  views.py
│  │  wsgi.py
│  ├─API
│  │  │  openAI.py
│  │  └─ weather.py
│  └─utils
│     │  coordinate_convert.py
│     └─ paginator.py
├─openAPI
│  │  apps.py
│  │  urls.py
│  └─views.py
├─post
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  serializers.py
│  │  signal.py
│  │  tests.py
│  │  urls.py
│  │  views.py
│  └─migrations
│     │  0001_initial.py
│     └─0002_initial.py
└─user
   │  admin.py
   │  apps.py
   │  backends.py
   │  managers.py
   │  models.py
   │  permissions.py
   ├─api
   │  │  renderers.py
   │  │  serializers.py
   │  │  urls.py
   │  └─ views.py      
   └─migrations
      └─0001_initial.py
```

## 💡 후기

- 김바름
  > Channels를 이용한 web socket 통신이나, docker를 이용한 배포과정 등을 처음 경험해봤는데, 작업과정에서 발생하는 관련 오류를 수정해가면서 channels나 docker에 대해서도 이해할 수 있는 좋은 기회였습니다. 또한 팀프로젝트에서 각자의 코드작성 예상시간과 실제시간의 차이가 많이 나서, 전체적인 일정이 복잡해졌는데, 이러한 관리의 중요성에 대해서도 알 수 있었습니다. 그리고 협업에서 branch 전략을 제대로 이용해본것은 처음인데, 머지과정에서 발생하는 충돌을 해결해보고, 풀 리퀘스트의 코드를 보고 서로 의견을 주고받는것도 정말 좋은 경험이었습니다.
- 김범석
  > JWT를 이용해 토큰을 관리하는 것을 이해하는 것이 조금 어려웠었고, 팀프로젝트로 협업하는 것이 처음이라 서투르다보니 문제점이 많았었습니다.  
  > 다른 팀원들에게 정말 많이 배웠고 제대로 팀프로젝트를 진행한 것이 처음이라서 새로운 경험을 할 수 있었습니다. 이를 통해 django drf와 git을 다루는 데에 익숙해져서 스스로가 조금 더 성장한 시간이었습니다.
- 류형환
  > 프론트가 없는 상태에서 기능만 개발하다 보니 기능이 완성되어도 데이터가 정상적으로 주고받고 데이터 처리를 확인하는 작업이 어색하여 어려웠습니다.  
  > drf가 무엇인지 조금이나마 아는 시간이 되었고 깃허브를 이용하여 팀과 협업을 한 경우가 이번이 처음이었는데 깃허브를 다루는 게 조금이나마 익숙해지는 시간이었던 거 같습니다.
- 임동성
  > 로그인과정에서의 token개념에 대해서 이해가 어려웠었고 django에 대해서 익숙해 지기가 어려웠습니다.  
  > 협업의 중요성에 대해서 깨닫게 되고 drf에서 사용되는 Serializer의 구조에 대해서 좀 더 직관적으로 알게되었습니다.
