from configparser import ConfigParser

#Hebrew Manuscript Images
def config_hb_images(img_loc):
    """
    Define path to images of Hebrew manuscripts
    :img_loc: trever, iaa, im, pam
    :return: specified location of img_loc
    """

    filename = 'ms_images.ini'
    section='hebrew'

    parser = ConfigParser()
    parser.read(filename)
    mss = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            mss[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in {1}'.format(section, filename))
    return mss[img_loc]