[![Deploy](https://github.com/nukosuke/jpx/actions/workflows/python-app.yml/badge.svg)](https://github.com/nukosuke/jpx/actions/workflows/python-app.yml)

```sh
curl https://nukosuke.github.io/jpx/8697.json
{"code": 8697, "name": "日本取引所グループ", "market": "プライム（内国株式）"}
```

### Apps Script
```js
function jpx(code, attr='name') {
  const resp = UrlFetchApp.fetch(`https://nukosuke.github.io/jpx/${code}.json`)
  const json = JSON.parse(resp)
  return json[attr]
}
```

![jpx](https://github.com/nukosuke/jpx/assets/17716649/6a360d3e-3681-40ec-bbc6-0bf9f75979df)
