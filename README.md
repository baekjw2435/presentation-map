# 제시 단어 수순 지도 (이식용 묶음)

한기사(817단어) 끝말잇기에서, 음절을 **어떤 단어로 제시했는지**에 따른 판정과 그 뒤의 수순을 보는 페이지입니다. 이 폴더를 정적 웹 서버에 올리면 주소 하나(`index.html`)에서 제시 단어를 고르고, 그 수순에 필요한 표 파일만 불러옵니다.

- 실행·이식 방법, 구성, 크기: [`README_KO.md`](README_KO.md)
- 파일마다 SHA-256: [`SHA256SUMS.txt`](SHA256SUMS.txt)
- ZIP: 릴리스 [`presentation-map-2026-11-14`](https://github.com/baekjw2435/presentation-map/releases/tag/presentation-map-2026-11-14)의 `presentation-map-2026-11-14.zip`
  - 562,846,290바이트, SHA-256 `6a55e802ec570c8fa8454a39e1f853c820afd11722f5841a229cb076ee964710`

묶음은 `SHA256SUMS.txt`에 적힌 파일 785개와 `SHA256SUMS.txt` 자신, 모두 786개입니다(585,334,856바이트, 가장 큰 파일 1,843,042바이트). 이 `README.md`, `.nojekyll`, `.github/`는 묶음에 들지 않습니다. `.nojekyll`은 GitHub Pages로 띄울 때 파일을 그대로 내보내게 하는 빈 파일입니다.

만든 곳: 연구 저장소의 `basic_root/alt_first_moves/site/` (`make_portable.py`, `pack_portable.py`).
