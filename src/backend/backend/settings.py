from pathlib import Path

# 프로젝트 베이스 디렉터리
BASE_DIR = Path(__file__).resolve().parent.parent

# 보안 키 & 디버그 모드
SECRET_KEY = 'django-insecure-...'
DEBUG = True
ALLOWED_HOSTS = []
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
# 앱 등록
INSTALLED_APPS = [
    'corsheaders',                   # CORS 허용
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'users',                         # 커스텀 유저 앱
    'products',                      # 상품/신고 앱

    'rest_framework',                # DRF
    'django_filters',                # 필터링
]

# 커스텀 유저 모델
AUTH_USER_MODEL = 'users.User'

# 미들웨어
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',       # Must be 맨 위
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'
WSGI_APPLICATION = 'backend.wsgi.application'

# 템플릿 설정 (admin 애플리케이션을 쓰려면 반드시 있어야 합니다)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],             # 프로젝트 템플릿 디렉터리 추가 시 여기에 경로를 넣으세요
        'APP_DIRS': True,       # 앱 내부의 templates/ 를 자동 탐색
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 데이터베이스 (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 비밀번호 검증
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 국제화
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 정적 파일
STATIC_URL = 'static/'

# DRF 설정
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}

# 모든 오리진 허용 (개발용)
CORS_ALLOW_ALL_ORIGINS = True

# 기본 PK 필드 타입
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

