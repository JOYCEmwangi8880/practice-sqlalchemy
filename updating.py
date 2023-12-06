from sqlalchemyex import Session,engine,User


local_session=Session(bind=engine)

user_to_update=local_session.query(User).filter(User.username=='evans').first()

user_to_update.username = 'evanicherru'
user_to_update.email='evanicherru@company.com'

local_session.commit()
