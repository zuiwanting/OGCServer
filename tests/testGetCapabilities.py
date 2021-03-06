import nose

def test_encoding():
    import os
    from ogcserver.configparser import SafeConfigParser
    from ogcserver.WMS import BaseWMSFactory
    from ogcserver.wms111 import ServiceHandler as ServiceHandler111
    from ogcserver.wms130 import ServiceHandler as ServiceHandler130

    base_path, tail = os.path.split(__file__)
    file_path = os.path.join(base_path, 'mapfile_encoding.xml')
    wms = BaseWMSFactory() 
    wms.loadXML(file_path)
    wms.finalize()

    conf = SafeConfigParser()
    conf.readfp(open(os.path.join(base_path, 'ogcserver.conf')))

    wms111 = ServiceHandler111(conf, wms, "localhost")
    response = wms111.GetCapabilities({})
    # Check the response is encoded in UTF-8
    # Search for the title in the response
    if conf.get('service', 'title') not in response.content:
        raise Exception('GetCapabilities is not correctly encoded')
    
    wms130 = ServiceHandler130(conf, wms, "localhost")
    wms130.GetCapabilities({})

    return True
 
