# 제시 단어 수순 지도 (이식용 묶음)

한기사(817단어) 끝말잇기에서, 음절을 **어떤 단어로 제시했는지**에 따른 판정과 그 뒤의 수순을 보는 페이지입니다. 이 폴더를 정적 웹 서버에 올리면 주소 하나(`index.html`)에서 제시 단어를 고르고, 그 수순에 필요한 표 파일만 불러옵니다.

- 실행·이식 방법, 구성, 크기: [`README_KO.md`](README_KO.md)
- 파일마다 SHA-256: [`SHA256SUMS.txt`](SHA256SUMS.txt)

## 릴리스

| 릴리스 | 진행률 | 전체 ZIP | 갱신본 |
|---|---|---|---|
| [`presentation-map-2026-11-14b`](https://github.com/baekjw2435/presentation-map/releases/tag/presentation-map-2026-11-14b) (최신) | 473/497 (자체 396 · 기존 77 · 미확정 24) | `presentation-map-2026-11-14b.zip` 593,278,776바이트, SHA-256 `cece4b5b002bdc0771eff5a8ea8757c4a2e3a8206e69d42995f307ac34cb51bf` | `presentation-map-2026-11-14b-update.zip` (첫 릴리스에서 바뀐 파일만) 30,616,187바이트, SHA-256 `092e759f3d35c6028c62cdbcd92c2b0fbdf074347f6c210d9a346a2eb14dd434` |
| [`presentation-map-2026-11-14`](https://github.com/baekjw2435/presentation-map/releases/tag/presentation-map-2026-11-14) | 469/497 (자체 392 · 기존 77 · 미확정 28) | `presentation-map-2026-11-14.zip` 562,846,290바이트, SHA-256 `6a55e802ec570c8fa8454a39e1f853c820afd11722f5841a229cb076ee964710` | |

진행률은 이번 추가 조사 대상의 진행률입니다. 모든 제시 단어나 모든 후속 갈래를 분석한 비율이 아닙니다.

지금 묶음은 `SHA256SUMS.txt`에 적힌 파일 805개와 `SHA256SUMS.txt` 자신, 모두 806개입니다(616,793,655바이트, 가장 큰 파일 1,843,042바이트). 이 `README.md`, `.nojekyll`, `.github/`는 묶음에 들지 않습니다. `.nojekyll`은 GitHub Pages로 띄울 때 파일을 그대로 내보내게 하는 빈 파일입니다.

만든 곳: 연구 저장소의 `basic_root/alt_first_moves/site/` (`make_portable.py`, `pack_portable.py`). ZIP은 이 저장소의 작업 `release-zip`이 `.github/pack_portable.py`로 다시 만들어, 연구 저장소에서 만든 것과 SHA-256이 같을 때만 올립니다.
