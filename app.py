from fastapi import FastAPI

# 프로그램의 메인 역활을 함
# 1. 서버 초기화: 설정, RAG엔진, LangGraph를 최초 생성
# 2. 서비스 인증: Spring Boot가 전달하는 서비스 토큰 검증
# 3. 게시글 색인: /index 전달받은 게시글 저장
# 4. 게시글 삭제: /index/{board_id}로 색인 데이터 삭제
# 5. AI 질의: /query로 전달받은 질문 처리

import logging # 서버 실행 정보 및 오류 기록
import secrets # 서버 토큰 안정 비교
from contextlib import asynccontextmanager # 서버 시작 및 종료 시 작업 관리
# Depends: API 요청 전에 인증 함수 실행,
# Request: 현재 요청 및 앱 상태 접근
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.concurrency import run_in_threadpool   # 동기 함수를 별도 스레드 풀에서 실행


app = FastAPI(title="Board RAG AI Service")

@app.get("/health")
def health():
    return {"status": "OK"}