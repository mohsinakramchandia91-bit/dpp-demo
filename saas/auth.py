import uuid, json, os

USERS = "data/users.json"

def _load():
  if not os.path.exists(USERS): return {}
  return json.load(open(USERS))

def _save(d):
  os.makedirs("data", exist_ok=True)
  json.dump(d, open(USERS,"w"), indent=2)

def signup(email, password):
  users = _load()
  cid = "cmp_" + uuid.uuid4().hex[:8]
  users[email] = {"password": password, "company_id": cid, "plan": "starter"}
  _save(users)
  return cid

def login(email, password):
  users = _load()
  u = users.get(email)
  if not u or u["password"] != password:
    raise Exception("Invalid login")
  return u
