from sqlalchemyex import User,Session,engine
from sqlalchemy import descending


local_session=Session(bind=engine)

#ascending order
# users=local_session.query(User).order_by(User.username).all()

# for user in users:
#     print(f"User {user.username}")


#descending order
users_desc=local_session.query(User).order_by(User.username).all()

for user in users_desc:
    print(f"user {user.username}")

