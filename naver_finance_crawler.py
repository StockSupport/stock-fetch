from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

def crawl_naver_finance_news():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # 최신 headless 모드 사용
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")  # 윈도우 크기 설정

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://finance.naver.com/news/mainnews.naver")
    wait = WebDriverWait(driver, 10)

    try:
        # 뉴스 리스트가 로드될 때까지 대기
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.newsList li a")))

        # 뉴스 링크 가져오기
        news_items = driver.find_elements(By.CSS_SELECTOR, "ul.newsList li a")

        for item in news_items:
            title = item.text.strip()
            link = item.get_attribute("href")

            if title and link:
                print(f"제목: {title}")
                print(f"링크: {link}")

                try:
                    # 새 탭 열고 뉴스 상세 페이지 이동
                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[1])
                    driver.get(link)

                    # 내용 가져오기
                    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#newsct_article")))
                    content = driver.find_element(By.CSS_SELECTOR, "div#newsct_article").text.strip()

                    print(f"내용: {content[:500]}...")  # 처음 500자만 출력
                    print("-" * 50)

                except Exception as e:
                    print(f"내용을 가져오는 중 오류 발생: {e}")
                finally:
                    # 현재 탭 닫고 원래 탭으로 이동
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

    except TimeoutException:
        print("뉴스 로딩에 너무 오랜 시간이 걸립니다.")
    finally:
        driver.quit()

# 실행
crawl_naver_finance_news()
