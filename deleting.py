from sqlalchemyex import User,Session,engine



local_session=Session(bind=engine)

useer_to_delete=local_session.query(User).filter(User.username=='evanicherru').first()

local_session.delete(useer_to_delete)

local_session.commit()