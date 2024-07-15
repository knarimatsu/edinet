def find_data(soup, tag_name, context_ref, context_ref_nonconsolidatedMember):
    """_summary_

    Returns:
        _type_: _description_
    """

    result = soup.find(tag_name, contextRef=context_ref)
    if result is None:
        result = soup.find(tag_name, contextRef=context_ref_nonconsolidatedMember)
    if result is not None:
        return result.text
    else:
        return ""
