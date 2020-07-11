# -*- coding: utf-8 -*-
from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()

arguments = {"keywords":"수지, 트와이스 나연, 아이유, 아이즈원 장원영, 레드벨벳 아이린, 이달의 소녀 츄, 신민아, 한채영, 차예련, 유인영, itzy 예지, 나인뮤지스 경리, 원더걸스 소희, 한예슬, 송혜교, 한지민, 손예진, 박보영, 설리, 백진희, 이민정, 러블리즈 케이, 여자아이들 우기, 위키미키 최유정, 신민아, 박시연, 김소연, 김예림, 송지효, 주니엘, 장재인, 공민지, 에프엑스 엠버, 프로미스나인 이새롬, 정려원, 소녀시대 태연, 김민희, 윤아, 고아라, 이연희", "limit":20, "print_urls":True, "format":"jpg"}
paths = response.download(arguments)
print(paths)
