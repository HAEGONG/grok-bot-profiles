# grok-bot-profiles

Grok Bot 직무 프로필 모음.

Grok Bot은 JSON을 임포트하지 않는다. 앱의 **Name / Title / Description / Avatar**에 붙여 넣는 텍스트다. 이 저장소는 그 텍스트를 `PROFILE.md`로 둔다.

공식 문서: [Create and manage Bots](https://docs.x.ai/grok-bot/bots) · [Get started](https://docs.x.ai/grok-bot/get-started) · [Use cases](https://docs.x.ai/grok-bot/use-cases)

## 앱 필드 매핑

| 앱 | 파일 |
| --- | --- |
| Name | `PROFILE.md` frontmatter `name` |
| Title | `PROFILE.md` frontmatter `title` |
| Description | `PROFILE.md` 본문 (`# NAME`부터 First task까지). YAML frontmatter는 넣지 않는다 |
| Avatar | 앱에서만 설정 |
| Plugins | frontmatter `integrations` → Settings → Plugins |

Description에는 계속 참이어야 하는 규칙만 넣는다. 이번 작업만의 지시는 대화에 둔다.

## 새 봇 추가

```bash
cp -R templates/bot bots/<category>/<slug>
```

카테고리: `productivity` · `marketing` · `sales` · `ops` · `personal` · `development`

1. `PROFILE.md`의 `NAME`, `ONE JOB`, `ONE_REPEATABLE_OUTCOME`, 소스, 산출물, 금지선, `FIRST_TASK`를 채운다.
2. `SETUP.md`와 `README.md`의 같은 placeholder를 맞춘다.
3. 앱에서 **New → Create new agent** 후 **Edit Profile**에 Name / Title / Description을 넣는다.
4. `integrations`에 적힌 플러그인을 연결하고 First task를 보낸다.

직무가 갈라져야 하는 기준: 목표, 도구/소스, 작업 스타일, 승인 경계, 반복 스케줄. General Helper는 쓰지 않는다.

## 폴더

```
templates/bot/     복사할 보일러플레이트
bots/<category>/<slug>/
  PROFILE.md       Name + Description 본문
  SETUP.md         새 봇에 보내는 첫 메시지
  README.md        플러그인, First task, 관련 봇
```
