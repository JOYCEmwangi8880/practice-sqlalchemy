from sqlalchemyex import User,Session,engine

local_session=Session(bind=engine)

#returning all objects
# users=local_session.query(User).all()[:3]

# for user in users:
#     print (user.username)

#return query fro one object

evans=local_session.query(User).filter(User.username=='evans').first()
print(evans)




