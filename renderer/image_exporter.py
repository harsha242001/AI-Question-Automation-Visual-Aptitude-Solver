from playwright.sync_api import sync_playwright

def export_image(html_content, output_path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(html_content)
        
        # We need to explicitly evaluate the javascript that assigns tag styles
        # in the individual html template before we screenshot!
        page.wait_for_load_state('networkidle')
        
        element = page.locator(".main-wrapper")
        if element.count() > 0:
            element.first.screenshot(path=output_path)
        else:
            page.screenshot(path=output_path)
            
        browser.close()
