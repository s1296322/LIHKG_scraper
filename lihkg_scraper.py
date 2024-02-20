from selenium.webdriver.firefox.options import Options
import pandas as pd
import time
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import argparse

# 类别映射字典
category_mapping = { '4': '手機台', '5': '時事台', '6': '體育台', '7': '娛樂台', '8': '動漫台', '9': 'Apps台', '10': '遊戲台', '11': '影視台', '12': '講故台', '13': '潮流台', '14': '上班台', '15': '財經台', '16': '飲食台', '17': '旅遊台', 
                    '18': '學術台', '19': '校園台', '20': '汽車台', '21': '音樂台', '22': '硬件台', '23': '攝影台', '24': '玩具台', '25': '寵物台', '26': '軟件台', '27': '活動台', '28': '站務台', '30': '感情台', 
                    '31': '創意台', '32': '黑洞', '33': '政事台', '34': '直播台', '35': '電訊台', '36': '健康台', '37': '房屋台', '38': 'World', '39': '家庭台', '40': '美容台', '41': '電器台' }

def scrape_posts(start_post, end_post, headless=True):
    # Create an empty DataFrame
    df = pd.DataFrame(columns=['Post_number', 'Title', 'Main_content', 'Comments', 'URL', 'Category'])

    options = Options()
    options.headless = headless
    driver = webdriver.Firefox(options=options)

    for post_number in range(start_post, end_post + 1):
        post_url = f"https://lihkg.com/thread/{post_number}/page/1"
        driver.get(post_url)
        time.sleep(2)  # Wait for page to load
        try:
            elem = driver.find_element("xpath", "//*")
            source_code = elem.get_attribute("outerHTML")

            pattern = r"<title>(.*?)</title>"
            match = re.search(pattern, source_code)
            extracted_title = match.group(1).split(" | ")[0] if match else None

            soup = BeautifulSoup(source_code, 'html.parser')
            description_tag = soup.find('meta', {'name': 'description'})
            content_text = BeautifulSoup(description_tag['content'], 'html.parser').text.strip() if description_tag else None
            extracted_text = re.sub(r'http\S+', '', content_text) if content_text else None

            div_tags = soup.select('div[data-ast-root="true"]')
            useful_contents = list(set(tag.text for tag in div_tags))
            filtered_contents = [re.sub(r'http\S+', '', content) for content in useful_contents]
            combined_content = ', '.join(filtered_contents)

            pattern = r'category_id=(\d+)'
            match = re.search(pattern, source_code)
            category_id = match.group(1) if match else 'None'

            # Add post information to one row of DataFrame
            new_row = {
                'Post_number': post_number,
                'Title': extracted_title,
                'Main_content': extracted_text,
                'Comments': combined_content,
                'URL': post_url,
                'Category': category_id
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        except Exception as e:
            print(f"Error scraping post {post_number}: {e}")

    driver.quit()
    return df

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrape posts from LIHKG.')
    parser.add_argument('--start', type=int, required=True, help='Start post number')
    parser.add_argument('--end', type=int, required=True, help='End post number')
    parser.add_argument('--output', type=str, required=True, help='Output CSV file name')
    parser.add_argument('--headless', type=bool, default=True, help='Run browser in headless mode')
    
    args = parser.parse_args()
    
    df = scrape_posts(args.start, args.end, args.headless)
    
    # Map category IDs to names
    df['Category'] = df['Category'].map(category_mapping).fillna('None')
    
    # Save the DataFrame to CSV with utf-8-sig encoding
    df.to_csv(args.output, index=False, encoding='utf-8-sig')
    print(f"Scraped posts saved to {args.output} with UTF-8-SIG encoding")
