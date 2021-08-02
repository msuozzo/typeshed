from collections.abc import Generator
from typing import Any

from selenium.common.exceptions import (
    InvalidArgumentException as InvalidArgumentException,
    NoSuchCookieException as NoSuchCookieException,
    WebDriverException as WebDriverException,
)
from selenium.webdriver.common.by import By as By
from selenium.webdriver.common.html5.application_cache import ApplicationCache as ApplicationCache

from .command import Command as Command
from .errorhandler import ErrorHandler as ErrorHandler
from .file_detector import FileDetector as FileDetector, LocalFileDetector as LocalFileDetector
from .mobile import Mobile as Mobile
from .remote_connection import RemoteConnection as RemoteConnection
from .switch_to import SwitchTo as SwitchTo
from .webelement import WebElement as WebElement

class WebDriver:
    command_executor: Any
    session_id: Any
    capabilities: Any
    error_handler: Any
    def __init__(
        self,
        command_executor: str = ...,
        desired_capabilities: Any | None = ...,
        browser_profile: Any | None = ...,
        proxy: Any | None = ...,
        keep_alive: bool = ...,
        file_detector: Any | None = ...,
        options: Any | None = ...,
    ) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...
    def file_detector_context(self, file_detector_class, *args, **kwargs) -> Generator[None, None, None]: ...
    @property
    def mobile(self): ...
    @property
    def name(self): ...
    def start_client(self) -> None: ...
    def stop_client(self) -> None: ...
    w3c: Any
    def start_session(self, capabilities, browser_profile: Any | None = ...) -> None: ...
    def create_web_element(self, element_id): ...
    def execute(self, driver_command, params: Any | None = ...): ...
    def get(self, url) -> None: ...
    @property
    def title(self): ...
    def find_element_by_id(self, id_): ...
    def find_elements_by_id(self, id_): ...
    def find_element_by_xpath(self, xpath): ...
    def find_elements_by_xpath(self, xpath): ...
    def find_element_by_link_text(self, link_text): ...
    def find_elements_by_link_text(self, text): ...
    def find_element_by_partial_link_text(self, link_text): ...
    def find_elements_by_partial_link_text(self, link_text): ...
    def find_element_by_name(self, name): ...
    def find_elements_by_name(self, name): ...
    def find_element_by_tag_name(self, name): ...
    def find_elements_by_tag_name(self, name): ...
    def find_element_by_class_name(self, name): ...
    def find_elements_by_class_name(self, name): ...
    def find_element_by_css_selector(self, css_selector): ...
    def find_elements_by_css_selector(self, css_selector): ...
    def execute_script(self, script, *args): ...
    def execute_async_script(self, script, *args): ...
    @property
    def current_url(self): ...
    @property
    def page_source(self): ...
    def close(self) -> None: ...
    def quit(self) -> None: ...
    @property
    def current_window_handle(self): ...
    @property
    def window_handles(self): ...
    def maximize_window(self) -> None: ...
    def fullscreen_window(self) -> None: ...
    def minimize_window(self) -> None: ...
    @property
    def switch_to(self): ...
    def switch_to_active_element(self): ...
    def switch_to_window(self, window_name) -> None: ...
    def switch_to_frame(self, frame_reference) -> None: ...
    def switch_to_default_content(self) -> None: ...
    def switch_to_alert(self): ...
    def back(self) -> None: ...
    def forward(self) -> None: ...
    def refresh(self) -> None: ...
    def get_cookies(self): ...
    def get_cookie(self, name): ...
    def delete_cookie(self, name) -> None: ...
    def delete_all_cookies(self) -> None: ...
    def add_cookie(self, cookie_dict) -> None: ...
    def implicitly_wait(self, time_to_wait) -> None: ...
    def set_script_timeout(self, time_to_wait) -> None: ...
    def set_page_load_timeout(self, time_to_wait) -> None: ...
    def find_element(self, by=..., value: Any | None = ...): ...
    def find_elements(self, by=..., value: Any | None = ...): ...
    @property
    def desired_capabilities(self): ...
    def get_screenshot_as_file(self, filename): ...
    def save_screenshot(self, filename): ...
    def get_screenshot_as_png(self): ...
    def get_screenshot_as_base64(self): ...
    def set_window_size(self, width, height, windowHandle: str = ...) -> None: ...
    def get_window_size(self, windowHandle: str = ...): ...
    def set_window_position(self, x, y, windowHandle: str = ...): ...
    def get_window_position(self, windowHandle: str = ...): ...
    def get_window_rect(self): ...
    def set_window_rect(self, x: Any | None = ..., y: Any | None = ..., width: Any | None = ..., height: Any | None = ...): ...
    @property
    def file_detector(self): ...
    @file_detector.setter
    def file_detector(self, detector) -> None: ...
    @property
    def orientation(self): ...
    @orientation.setter
    def orientation(self, value) -> None: ...
    @property
    def application_cache(self): ...
    @property
    def log_types(self): ...
    def get_log(self, log_type): ...