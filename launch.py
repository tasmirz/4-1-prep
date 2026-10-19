#!/usr/bin/env python3
"""
KUET CSE Academic Study Hub — Browser Launcher
=============================================
Clickable executable script to launch index.html in your default web browser.

Usage:
  ./launch.py             # Open index.html directly in browser (instant offline mode)
  ./launch.py --server    # Start a local HTTP server and open in browser (port 8000+)
  ./launch.py --network   # Host on local network (0.0.0.0) for phone/tablet access
  ./launch.py -h, --help  # Show full usage instructions
"""

import sys
import os
import argparse
import socket
import webbrowser
import subprocess
from pathlib import Path

# Paths
ROOT_DIR = Path(__file__).resolve().parent
INDEX_FILE = ROOT_DIR / "index.html"


def find_free_port(start_port: int = 8000, max_port: int = 8100) -> int:
    """Find an available port starting from start_port."""
    for port in range(start_port, max_port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind(("", port))
                return port
            except OSError:
                continue
    return start_port


def get_local_ip() -> str:
    """Get the primary local LAN IP address."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"


def open_in_browser(target_url: str, browser_name: str = "firefox"):
    """Open URL using preferred browser (Firefox), with webbrowser/xdg-open fallback."""
    print(f"🌐 Opening in {browser_name or 'default browser'}: {target_url}")
    opened = False

    # 1. Try specified browser executable first (e.g., firefox)
    if browser_name:
        try:
            subprocess.Popen(
                [browser_name, target_url],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
            )
            return True
        except Exception as e:
            print(f"⚠️  {browser_name} direct launch notice: {e}")

    # 2. Try Python webbrowser module
    try:
        opened = webbrowser.open(target_url, new=2)
    except Exception as e:
        print(f"⚠️  webbrowser.open warning: {e}")

    # 3. Fallback to xdg-open on Linux desktop
    if not opened and sys.platform.startswith("linux"):
        try:
            subprocess.Popen(
                ["xdg-open", target_url],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True,
            )
            opened = True
        except Exception:
            pass

    return opened


def run_http_server(host: str = "127.0.0.1", port: int = 8000, browser_name: str = "firefox"):
    """Serve ROOT_DIR via Python's standard http.server."""
    import http.server
    import socketserver
    from functools import partial

    actual_port = find_free_port(port)

    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(ROOT_DIR), **kwargs)

        def log_message(self, format, *args):
            # Clean, non-intrusive log format
            sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")

    handler = partial(CustomHandler)

    local_url = f"http://localhost:{actual_port}/index.html"
    lan_ip = get_local_ip()
    lan_url = f"http://{lan_ip}:{actual_port}/index.html"

    print("=" * 64)
    print("🎓 KUET CSE ACADEMIC STUDY HUB · HTTP SERVER")
    print("=" * 64)
    print(f"📁 Serving Directory: {ROOT_DIR}")
    print(f"📍 Local URL:        {local_url}")
    if host == "0.0.0.0" and lan_ip != "127.0.0.1":
        print(f"📱 LAN (Mobile) URL:  {lan_url}")
    print("=" * 64)
    print("✨ Press Ctrl+C in terminal anytime to stop server.")
    print("=" * 64)

    # Launch browser after a brief delay
    open_in_browser(local_url, browser_name=browser_name)

    # Allow fast socket reuse
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer((host, actual_port), handler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped gracefully. Goodbye!")
    except Exception as e:
        print(f"\n❌ Server error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Launch KUET CSE Academic Study Hub in your web browser.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ./launch.py              Launch index.html directly via file URI in Firefox (instant)
  ./launch.py --browser brave Open in another browser
  ./launch.py -s           Start local HTTP server on port 8000 and open browser
  ./launch.py -s -p 8080   Start HTTP server on custom port 8080
  ./launch.py --network    Host on local Wi-Fi for phone/tablet access
        """,
    )
    parser.add_argument(
        "-b",
        "--browser",
        type=str,
        default="firefox",
        help="Web browser to launch with (default: firefox)",
    )
    parser.add_argument(
        "-s",
        "--server",
        action="store_true",
        help="Start a local HTTP server instead of direct file:// opening",
    )
    parser.add_argument(
        "-n",
        "--network",
        action="store_true",
        help="Host on 0.0.0.0 to enable access from phone/tablet on same Wi-Fi",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Port to use when running in server mode (default: 8000)",
    )
    parser.add_argument(
        "--host",
        type=str,
        default=None,
        help="Host IP to bind server to (defaults to 127.0.0.1, or 0.0.0.0 if --network)",
    )

    args = parser.parse_args()

    # Validate that index.html exists
    if not INDEX_FILE.exists():
        print(f"❌ Error: Could not find '{INDEX_FILE}'", file=sys.stderr)
        sys.exit(1)

    if args.server or args.network:
        host = args.host if args.host else ("0.0.0.0" if args.network else "127.0.0.1")
        run_http_server(host=host, port=args.port, browser_name=args.browser)
    else:
        file_url = INDEX_FILE.as_uri()
        print("=" * 64)
        print("🎓 KUET CSE ACADEMIC STUDY HUB")
        print("=" * 64)
        print(f"📄 Portal File: {INDEX_FILE}")
        print(f"🔗 File URI:    {file_url}")
        print(f"🌐 Browser:     {args.browser}")
        print("=" * 64)
        open_in_browser(file_url, browser_name=args.browser)
        print("✅ Launched successfully!")
        print("💡 Tip: Run with `./launch.py --server` to start an HTTP server.")
        print("=" * 64)


if __name__ == "__main__":
    main()
