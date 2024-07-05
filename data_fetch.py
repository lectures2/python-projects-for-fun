import requests
import tkinter as tk
from tkinter import messagebox, ttk
import pyperclip
from zapv2 import ZAPv2

def fetch_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        return html_content
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None

def scan_link():
    link = entry.get()
    html_content = fetch_html_content(link)
    if html_content:
        vulnerabilities = find_vulnerabilities(link)
        if vulnerabilities:
            report = generate_report(vulnerabilities, link)
            messagebox.showinfo("Vulnerabilities Detected", "Vulnerabilities detected! Click 'Copy Report' to copy the report content.")
            copy_button.config(state=tk.NORMAL)
            report_text.delete('1.0', tk.END)
            report_text.insert(tk.END, report)
        else:
            messagebox.showinfo("No Vulnerabilities", "No vulnerabilities found in the HTML content.")
            copy_button.config(state=tk.DISABLED)

def find_vulnerabilities(link):
    vulnerabilities = []

    # ZAP Configuration
    zap = ZAPv2()

    # Set the target URL
    zap.urlopen(link)

    # Spider the website
    zap.spider.scan(link)

    # Wait for the spider to complete
    while int(zap.spider.status()) < 100:
        progress = zap.spider.status()
        # Update progress or display a loading spinner

    # Scan for vulnerabilities
    zap.ascan.scan(link)

    # Wait for the active scan to complete
    while int(zap.ascan.status()) < 100:
        progress = zap.ascan.status()
        # Update progress or display a loading spinner

    # Get the alerts (vulnerabilities)
    alerts = zap.core.alerts()

    for alert in alerts:
        vulnerabilities.append({
            "name": alert["name"],
            "risk": alert["risk"],
            "description": alert["description"],
            "solution": alert["solution"]
        })

    return vulnerabilities

def generate_report(vulnerabilities, link):
    report = f"Vulnerability Report for {link}\n\n"

    for vulnerability in vulnerabilities:
        name = vulnerability["name"]
        risk = vulnerability["risk"]
        description = vulnerability["description"]
        solution = vulnerability["solution"]

        report += f"Name: {name}\n"
        report += f"Risk: {risk}\n"
        report += f"Description: {description}\n"
        report += f"Solution: {solution}\n\n"

    return report

def copy_report():
    report_content = report_text.get("1.0", tk.END)
    pyperclip.copy(report_content)
    messagebox.showinfo("Copied", "Report content copied to clipboard.")

def main():
    global entry, report_text, copy_button

    # Create the main application window
    window = tk.Tk()
    window.title("Bug Bounty Tool")
    window.geometry("400x400")

    # Create the input label and entry field
    label = tk.Label(window, text="Enter the link to scan:")
    label.pack()

    entry = tk.Entry(window, width=50)
    entry.pack()

    # Create the Scan button
    scan_button = tk.Button(window, text="Scan", command=scan_link)
    scan_button.pack()

    # Create the Report section
    report_frame = ttk.Frame(window)
    report_frame.pack(fill=tk.BOTH, expand=True)

    report_label = ttk.Label(report_frame, text="Vulnerability Report:")
    report_label.pack()

    report_text = tk.Text(report_frame, height=10)
    report_text.pack(fill=tk.BOTH, expand=True)

    # Create the Copy button
    copy_button = tk.Button(window, text="Copy Report", command=copy_report, state=tk.DISABLED)
    copy_button.pack()

    # Create the Exit button
    exit_button = tk.Button(window, text="Exit", command=window.quit)
    exit_button.pack()

    # Run the application
    window.mainloop()

if __name__ == "__main__":
    main()
