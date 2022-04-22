from sqlalchemy import create_engine, Column,\
    Integer, Boolean, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///temperature.db?check_same_thread=False', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Temperature(Base):
    __tablename__ = 'temperature'
    id = Column(Integer, primary_key=True)
    applicationID = Column(String)
    applicationName = Column(String)
    deviceName = Column(String)
    devEUI = Column(String)
    rxInfos = relationship("RXInfo", back_populates="temperature", cascade="all, delete-orphan")
    txFrequency = Column(Integer)
    txModulation = Column(String)
    txBandwidth = Column(Integer)
    txSpreadingFactor = Column(Integer)
    txCodeRate = Column(String)
    txPolarizationInversion = Column(Boolean)
    adr = Column(Boolean)
    dr = Column(Integer)
    fCnt = Column(Integer)
    fPort = Column(Integer)
    data = Column(String)
    objectJSON = Column(String)


class RXInfo(Base):
    __tablename__ = "rxInfo"
    id = Column(Integer, primary_key=True)
    gatewayID = Column(String)
    time = Column(String)
    rssi = Column(Integer)
    loRaSNR = Column(Integer)
    channel = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    altitude = Column(Float)
    fineTimestampType = Column(String)
    context = Column(String)
    uplinkID = Column(String)
    temperature_id = Column(Integer, ForeignKey("temperature.id"), nullable=False)
    temperature = relationship("Temperature", back_populates="rxInfos")

def create_db():
    Base.metadata.create_all(engine)


def delete_db():
    Base.metadata.drop_all(engine)


def get_all_times():
    array = []
    for time in session.query(RXInfo.time):
        array.append(time[0])
    return array


def get_all_data():
    array = []
    for data in session.query(Temperature.data):
        array.append(int(data[0]))
    return array


def add_temperature(temperature: Temperature):
    session.add(temperature)
    session.commit()

def add_rxInfo(rxInfo: RXInfo):
    session.add(rxInfo)
    session.commit()


def print_all_temperatures():
    for date, temp in session.query(Temperature.date, Temperature.temp):
        print(date, temp)


if __name__ == '__main__':
    delete_db()
    create_db()
