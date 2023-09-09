def get_page_data(current_page, max_page):
    right_index = min(max(current_page - 5, 1) + 9, max_page)
    left_index  = max(right_index - 10 + 1, 1)
    page_range = range(left_index, right_index + 1)
    if current_page == 1:
        prev_button = None
    else:
        prev_button = max(current_page-10, 1)
    
    if current_page == max_page:
        next_button = None
    else:
        next_button = min(current_page+10, max_page)

    return {
        "page_range": list(page_range), 
        "current_page": current_page,
        "prev_button": prev_button,
        "next_button": next_button,
    }
