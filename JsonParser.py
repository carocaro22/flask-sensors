from model import Temperature, RXInfo


def parse_json(content):
    rxInfoArray = []
    applicationID = content['applicationID']
    applicationName = content['applicationName']
    deviceName = content['deviceName']
    devEUI = content['deviceName']
    rxInfo = content['rxInfo']

    for info in rxInfo:
        gatewayID = info['gatewayID']
        time = info['time']
        timeSinceGPSEpoch = info['timeSinceGPSEpoch']
        rssi = info['rssi']
        loRaSNR = info['loRaSNR']
        channel = info['channel']
        rfChain = info['rfChain']
        board = info['board']
        antenna = info['antenna']
        location = info['location']
        latitude = location['latitude']
        longitude = location['longitude']
        altitude = location['altitude']
        fineTimestampType = info['fineTimestampType']
        context = info['context']
        uplinkID = info['uplinkID']

        rx = RXInfo(
            gatewayID = gatewayID,
            time = time,
            rssi = rssi,
            loRaSNR = rssi,
            channel = channel,
            latitude = latitude,
            longitude = longitude,
            altitude = altitude,
            fineTimestampType = fineTimestampType,
            context = context,
            uplinkID = uplinkID
        )
        rxInfoArray.append(rx)

    txInfo = content['txInfo']
    frequency = txInfo['frequency']
    modulation = txInfo['modulation']
    loRaModulationInfo = txInfo['loRaModulationInfo']
    bandwidth = loRaModulationInfo['bandwidth']
    spreadingFactor = loRaModulationInfo['spreadingFactor']
    codeRate = loRaModulationInfo['codeRate']
    polarizationInversion = loRaModulationInfo['polarizationInversion']
    adr = content['adr']
    dr = content['dr']
    fCnt = content['fCnt']
    fPort = content['fPort']
    data = content['data']
    objectJSON = content['objectJSON']

    temp = Temperature(
        applicationID=applicationID,
        applicationName=applicationName,
        deviceName=deviceName,
        devEUI = devEUI,
        rxInfos = rxInfoArray,
        txFrequency=frequency,
        txModulation=modulation,
        txBandwidth=bandwidth,
        txSpreadingFactor=spreadingFactor,
        txCodeRate=codeRate,
        txPolarizationInversion=polarizationInversion,
        adr=adr,
        dr=dr,
        fCnt=fCnt,
        fPort=fPort,
        data=data,
        objectJSON=objectJSON
    )

    return temp

# gatewayID = gatewayID,
# time = time,
# rssi = ,
# loRaSNR = ,
# channel = ,
# latitude = ,
# longitude = ,
# altitude = ,
# fineTimestampType = ,
# uplinkID = ,