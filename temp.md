---
tags:
  - reference
  - database
  - mariadb
date: 2026-06-04
---

# MariaDB Setup Commands

```bash
# 1. Create the database
mariadb -u root -p -e "CREATE DATABASE IF NOT EXISTS uno;"

# 2. Create a dedicated user for your app
mariadb -u root -p -e "CREATE USER 'uno_app'@'%' IDENTIFIED BY 'unopassword0509';"

# 3. Grant permissions only to the uno database
mariadb -u root -p -e "GRANT ALL PRIVILEGES ON uno.* TO 'uno_app'@'%'; FLUSH PRIVILEGES;"
```

---

## Related

- [[ICT Index]] - ICT subject overview
