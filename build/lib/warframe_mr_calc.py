import requests
import tkinter as tk
from tkinter import ttk
import threading
import time

# Base URL for the API
BASE_URL = "https://api.warframe.market/v1"

# Updated item list with name, type, and value.
items_data = [
    {"name": "frost_prime_set", "type": "Warframe", "value": 6000},
    {"name": "hydroid_prime_set", "type": "Warframe", "value": 6000},
    {"name": "saryn_prime_set", "type": "Warframe", "value": 6000},
    {"name": "helios_prime_set", "type": "Warframe", "value": 6000},
    {"name": "rhino_prime_set", "type": "Warframe", "value": 6000},
    {"name": "wukong_prime_set", "type": "Warframe", "value": 6000},
    {"name": "ember_prime_set", "type": "Warframe", "value": 6000},
    {"name": "mag_prime_set", "type": "Warframe", "value": 6000},
    {"name": "oberon_prime_set", "type": "Warframe", "value": 6000},
    {"name": "trinity_prime_set", "type": "Warframe", "value": 6000},
    {"name": "carrier_prime_set", "type": "Warframe", "value": 6000},
    {"name": "dethcube_prime_set", "type": "Warframe", "value": 6000},
    {"name": "volt_prime_set", "type": "Warframe", "value": 6000},
    {"name": "titania_prime_set", "type": "Warframe", "value": 6000},
    {"name": "wyrm_prime_set", "type": "Warframe", "value": 6000},
    {"name": "inaros_prime_set", "type": "Warframe", "value": 6000},
    {"name": "valkyr_prime_set", "type": "Warframe", "value": 6000},
    {"name": "limbo_prime_set", "type": "Warframe", "value": 6000},
    {"name": "atlas_prime_set", "type": "Warframe", "value": 6000},
    {"name": "chroma_prime_set", "type": "Warframe", "value": 6000},
    {"name": "banshee_prime_set", "type": "Warframe", "value": 6000},
    {"name": "vauban_prime_set", "type": "Warframe", "value": 6000},
    {"name": "loki_prime_set", "type": "Warframe", "value": 6000},
    {"name": "nova_prime_set", "type": "Warframe", "value": 6000},
    {"name": "nyx_prime_set", "type": "Warframe", "value": 6000},
    {"name": "zephyr_prime_set", "type": "Warframe", "value": 6000},
    {"name": "ivara_prime_set", "type": "Warframe", "value": 6000},
    {"name": "mirage_prime_set", "type": "Warframe", "value": 6000},
    {"name": "equinox_prime_set", "type": "Warframe", "value": 6000},
    {"name": "ash_prime_set", "type": "Warframe", "value": 6000},
    {"name": "mesa_prime_set", "type": "Warframe", "value": 6000},
    {"name": "nekros_prime_set", "type": "Warframe", "value": 6000},
    {"name": "nezha_prime_set", "type": "Warframe", "value": 6000},
    {"name": "octavia_prime_set", "type": "Warframe", "value": 6000},
    {"name": "gara_prime_set", "type": "Warframe", "value": 6000},
    {"name": "nidus_prime_set", "type": "Warframe", "value": 6000},
    {"name": "harrow_prime_set", "type": "Warframe", "value": 6000},
    {"name": "garuda_prime_set", "type": "Warframe", "value": 6000},
    {"name": "khora_prime_set", "type": "Warframe", "value": 6000},
    {"name": "revenant_prime_set", "type": "Warframe", "value": 6000},
    {"name": "baruuk_prime_set", "type": "Warframe", "value": 6000},
    {"name": "hildryn_prime_set", "type": "Warframe", "value": 6000},
    {"name": "shade_prime_set", "type": "Warframe", "value": 6000},
    {"name": "wisp_prime_set", "type": "Warframe", "value": 6000},
    {"name": "grendel_prime_set", "type": "Warframe", "value": 6000},
    {"name": "gauss_prime_set", "type": "Warframe", "value": 6000},
    {"name": "protea_prime_set", "type": "Warframe", "value": 6000},
    {"name": "sevagoth_prime_set", "type": "Warframe", "value": 6000},
    {"name": "nautilus_prime_set", "type": "Warframe", "value": 6000},
    {"name": "xaku_prime_set", "type": "Warframe", "value": 6000},
    {"name": "lavos_prime_set", "type": "Warframe", "value": 6000},
    {"name": "wolf_sledge_set", "type": "Weapon", "value": 3000},
    {"name": "vasto_prime_set", "type": "Weapon", "value": 3000},
    {"name": "zhuge_prime_set", "type": "Weapon", "value": 3000},
    {"name": "dual_kamas_prime_set", "type": "Weapon", "value": 3000},
    {"name": "snipetron_vandal_set", "type": "Weapon", "value": 3000},
    {"name": "destreza_prime_set", "type": "Weapon", "value": 3000},
    {"name": "stradavar_prime_set", "type": "Weapon", "value": 3000},
    {"name": "silva_and_aegis_prime_set", "type": "Weapon", "value": 3000},
    {"name": "latron_prime_set", "type": "Weapon", "value": 3000},
    {"name": "lex_prime_set", "type": "Weapon", "value": 3000},
    {"name": "odonata_prime_set", "type": "Weapon", "value": 3000},
    {"name": "vectis_prime_set", "type": "Weapon", "value": 3000},
    {"name": "sicarus_prime_set", "type": "Weapon", "value": 3000},
    {"name": "braton_prime_set", "type": "Weapon", "value": 3000},
    {"name": "aklex_prime_set", "type": "Weapon", "value": 3000},
    {"name": "ninkondi_prime_set", "type": "Weapon", "value": 3000},
    {"name": "fang_prime_set", "type": "Weapon", "value": 3000},
    {"name": "euphona_prime_set", "type": "Weapon", "value": 3000},
    {"name": "bo_prime_set", "type": "Weapon", "value": 3000},
    {"name": "boar_prime_set", "type": "Weapon", "value": 3000},
    {"name": "boltor_prime_set", "type": "Weapon", "value": 3000},
    {"name": "strun_wraith_set", "type": "Weapon", "value": 3000},
    {"name": "kogake_prime_set", "type": "Weapon", "value": 3000},
    {"name": "lato_vandal_set", "type": "Weapon", "value": 3000},
    {"name": "braton_vandal_set", "type": "Weapon", "value": 3000},
    {"name": "akvasto_prime_set", "type": "Weapon", "value": 3000},
    {"name": "furax_wraith_set", "type": "Weapon", "value": 3000},
    {"name": "ankyros_prime_set", "type": "Weapon", "value": 3000},
    {"name": "paris_prime_set", "type": "Weapon", "value": 3000},
    {"name": "ballistica_prime_set", "type": "Weapon", "value": 3000},
    {"name": "venka_prime_set", "type": "Weapon", "value": 3000},
    {"name": "akbronco_prime_set", "type": "Weapon", "value": 3000},
    {"name": "dakra_prime_set", "type": "Weapon", "value": 3000},
    {"name": "dera_vandal_set", "type": "Weapon", "value": 3000},
    {"name": "latron_wraith_set", "type": "Weapon", "value": 3000},
    {"name": "twin_vipers_wraith_set", "type": "Weapon", "value": 3000},
    {"name": "baza_prime_set", "type": "Weapon", "value": 3000},
    {"name": "aksomati_prime_set", "type": "Weapon", "value": 3000},
    {"name": "hikou_prime_set", "type": "Weapon", "value": 3000},
    {"name": "reaper_prime_set", "type": "Weapon", "value": 3000},
    {"name": "sybaris_prime_set", "type": "Weapon", "value": 3000},
    {"name": "shedu_set", "type": "Weapon", "value": 3000},
    {"name": "redeemer_prime_set", "type": "Weapon", "value": 3000},
    {"name": "orthos_prime_set", "type": "Weapon", "value": 3000},
    {"name": "amesha_set", "type": "Weapon", "value": 3000},
    {"name": "elytron_set", "type": "Weapon", "value": 3000},
    {"name": "itzal_set", "type": "Weapon", "value": 3000},
    {"name": "tigris_prime_set", "type": "Weapon", "value": 3000},
    {"name": "karak_wraith_set", "type": "Weapon", "value": 3000},
    {"name": "fragor_prime_set", "type": "Weapon", "value": 3000},
    {"name": "pangolin_prime_set", "type": "Weapon", "value": 3000},
    {"name": "centaur_set", "type": "Weapon", "value": 3000},
    {"name": "onorix_set", "type": "Weapon", "value": 3000},
    {"name": "agkuza_set", "type": "Weapon", "value": 3000},
    {"name": "corvas_set", "type": "Weapon", "value": 3000},
    {"name": "rathbone_set", "type": "Weapon", "value": 3000},
    {"name": "glaive_prime_set", "type": "Weapon", "value": 3000},
    {"name": "scindo_prime_set", "type": "Weapon", "value": 3000},
    {"name": "akstiletto_prime_set", "type": "Weapon", "value": 3000},
    {"name": "stropha_set", "type": "Weapon", "value": 3000},
    {"name": "velox_set", "type": "Weapon", "value": 3000},
    {"name": "stahlta_set", "type": "Weapon", "value": 3000},
    {"name": "karyst_prime_set", "type": "Weapon", "value": 3000},
    {"name": "panthera_prime_set", "type": "Weapon", "value": 3000},
    {"name": "phaedra_set", "type": "Weapon", "value": 3000},
    {"name": "cernos_prime_set", "type": "Weapon", "value": 3000},
    {"name": "imperator_vandal_set", "type": "Weapon", "value": 3000},
    {"name": "akbolto_prime_set", "type": "Weapon", "value": 3000},
    {"name": "gorgon_wraith_set", "type": "Weapon", "value": 3000},
    {"name": "nikana_prime_set", "type": "Weapon", "value": 3000},
    {"name": "cyngas_set", "type": "Weapon", "value": 3000},
    {"name": "broken_war_set", "type": "Weapon", "value": 3000},
    {"name": "kaszas_set", "type": "Weapon", "value": 3000},
    {"name": "velocitus_set", "type": "Weapon", "value": 3000},
    {"name": "fluctus_set", "type": "Weapon", "value": 3000},
    {"name": "dual_decurion_set", "type": "Weapon", "value": 3000},
    {"name": "spira_prime_set", "type": "Weapon", "value": 3000},
    {"name": "sheev_set", "type": "Weapon", "value": 3000},
    {"name": "nami_skyla_prime_set", "type": "Weapon", "value": 3000},
    {"name": "kronen_prime_set", "type": "Weapon", "value": 3000},
    {"name": "tiberon_prime_set", "type": "Weapon", "value": 3000},
    {"name": "tipedo_prime_set", "type": "Weapon", "value": 3000},
    {"name": "tekko_prime_set", "type": "Weapon", "value": 3000},
    {"name": "arum_spinosa_set", "type": "Weapon", "value": 3000},
    {"name": "sporothrix_set", "type": "Weapon", "value": 3000},
    {"name": "bonewidow_set", "type": "Weapon", "value": 3000},
    {"name": "cortege_set", "type": "Weapon", "value": 3000},
    {"name": "voidrig_set", "type": "Weapon", "value": 3000},
    {"name": "cedo_set", "type": "Weapon", "value": 3000},
    {"name": "rubico_prime_set", "type": "Weapon", "value": 3000},
    {"name": "burston_prime_set", "type": "Weapon", "value": 3000},
    {"name": "soma_prime_set", "type": "Weapon", "value": 3000},
    {"name": "akjagara_prime_set", "type": "Weapon", "value": 3000},
    {"name": "gram_prime_set", "type": "Weapon", "value": 3000},
    {"name": "pyrana_prime_set", "type": "Weapon", "value": 3000},
    {"name": "guandao_prime_set", "type": "Weapon", "value": 3000},
    {"name": "zakti_prime_set", "type": "Weapon", "value": 3000},
    {"name": "spectra_vandal_set", "type": "Weapon", "value": 3000},
    {"name": "bronco_prime_set", "type": "Weapon", "value": 3000},
    {"name": "pathocyst_set", "type": "Weapon", "value": 3000}
]

def find_key(data, key):
    """Recursively search for a key in a nested dict/list structure."""
    if isinstance(data, dict):
        if key in data:
            return data[key]
        for v in data.values():
            result = find_key(v, key)
            if result is not None:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_key(item, key)
            if result is not None:
                return result
    return None

class OrderFetcherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Warframe Market Order Fetcher")
        self.total_items = len(items_data)
        self.current_index = 0

        # Progress UI.
        self.progress_frame = tk.Frame(self.master)
        self.progress_frame.pack(pady=10)
        self.progress_label = tk.Label(self.progress_frame, text="Starting order fetch...")
        self.progress_label.pack(pady=5)
        self.progress_bar = ttk.Progressbar(self.progress_frame, orient="horizontal", length=400, mode="determinate")
        self.progress_bar.pack(pady=5)
        self.progress_bar["maximum"] = self.total_items

        # Main table.
        self.table_frame = tk.Frame(self.master)
        self.table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        columns = ("Item", "Type", "Value", "Avg Price", "Lowest Price", "Highest Price", "Value/AvgPrice")
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.column("Item", width=250)
        self.tree.column("Type", width=100)
        self.tree.column("Value", width=80)
        self.tree.column("Avg Price", width=100)
        self.tree.column("Lowest Price", width=100)
        self.tree.column("Highest Price", width=100)
        self.tree.column("Value/AvgPrice", width=120)
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Dictionary to track row IDs.
        self.row_ids = {}
        for item in items_data:
            row_id = self.tree.insert("", "end", values=(item["name"], item["type"], item["value"], "Pending", "Pending", "Pending", "Pending"))
            self.row_ids[item["name"]] = row_id

        # Create a debug window.
        self.create_debug_window()

    def create_debug_window(self):
        self.debug_window = tk.Toplevel(self.master)
        self.debug_window.title("Debug Output")
        self.debug_text = tk.Text(self.debug_window, wrap="none", height=30)
        self.debug_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(self.debug_window, orient="vertical", command=self.debug_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.debug_text.config(yscrollcommand=scrollbar.set)

    def append_debug(self, text):
        self.debug_text.insert(tk.END, text + "\n")
        self.debug_text.see(tk.END)

    def start_fetching(self):
        threading.Thread(target=self.fetch_all_orders, daemon=True).start()

    def fetch_all_orders(self):
        for item in items_data:
            name = item["name"]
            result = self.fetch_price(name)
            if isinstance(result, tuple):
                avg_price, lowest, highest, incomplete = result
                if isinstance(avg_price, (int, float)) and avg_price != 0:
                    ratio = round(item["value"] / avg_price, 2)
                else:
                    ratio = "N/A"
                # Append an asterisk if data is incomplete.
                avg_disp = f"{avg_price}*" if incomplete else f"{avg_price}"
                low_disp = f"{lowest}*" if incomplete else f"{lowest}"
                high_disp = f"{highest}*" if incomplete else f"{highest}"
            else:
                avg_disp, low_disp, high_disp, ratio = "N/A", "N/A", "N/A", "N/A"
            self.master.after(0, self.update_row, name, item["type"], item["value"], avg_disp, low_disp, high_disp, ratio)
            self.current_index += 1
            self.master.after(0, self.update_progress, name)
            time.sleep(0.2)
        self.master.after(0, self.sort_table_by_ratio)
        self.master.after(0, self.show_summary_window)

    def fetch_price(self, name):
        """
        For a given item, fetch orders and recursively search for "platinum", "order_type", and "status".
        Only consider orders where:
          - platinum is present and convertible to float,
          - order_type is "sell", and
          - status is either "online" or "ingame".
        Then, take the lowest up to 8 platinum values. If fewer than 8 orders are available but at least one exists,
        compute the average and mark it as incomplete.
        Returns a tuple: (avg_price, lowest, highest, incomplete_flag)
        """
        try:
            response = requests.get(f"{BASE_URL}/items/{name}/orders")
            debug_response = response.text
            self.master.after(0, self.append_debug, f"Response for {name}:\n{debug_response}\n{'-'*40}")
            if response.ok:
                data = response.json()
                orders = data.get("payload", {}).get("orders", [])
                valid_orders = []
                for order in orders:
                    platinum = find_key(order, "platinum")
                    order_type = find_key(order, "order_type")
                    user_status = find_key(order, "status")
                    if platinum is None or order_type != "sell" or user_status not in {"online", "ingame"}:
                        continue
                    try:
                        platinum_val = float(platinum)
                    except Exception:
                        continue
                    valid_orders.append({"platinum": platinum_val})
                self.master.after(0, self.append_debug, f"For {name}: Found {len(valid_orders)} valid sell orders with status online/ingame.")
                if len(valid_orders) < 1:
                    self.master.after(0, self.append_debug, f"For {name}: No valid orders available.")
                    return "N/A"
                sorted_orders = sorted(valid_orders, key=lambda o: o.get("platinum", float('inf')))
                sorted_platinum = [o.get("platinum") for o in sorted_orders]
                self.master.after(0, self.append_debug, f"For {name}: Sorted platinum values: {sorted_platinum}")
                count = min(len(sorted_orders), 8)
                selected_orders = sorted_orders[:count]
                selected_platinum = [o.get("platinum") for o in selected_orders]
                self.master.after(0, self.append_debug, f"For {name}: Using platinum values (lowest {count}): {selected_platinum}")
                avg_price = sum(selected_platinum) / len(selected_platinum)
                lowest = min(selected_platinum)
                highest = max(selected_platinum)
                incomplete = (len(sorted_orders) < 8)
                return (round(avg_price, 2), lowest, highest, incomplete)
            else:
                return f"Error {response.status_code}"
        except Exception as e:
            return f"Exception: {e}"

    def update_row(self, name, type_, value, avg_price, lowest, highest, ratio):
        row_id = self.row_ids.get(name)
        if row_id:
            self.tree.item(row_id, values=(name, type_, value, avg_price, lowest, highest, ratio))

    def update_progress(self, current_item):
        self.progress_label.config(text=f"Fetched: {current_item} ({self.current_index}/{self.total_items})")
        self.progress_bar["value"] = self.current_index
        self.master.update_idletasks()

    def sort_table_by_ratio(self):
        children = self.tree.get_children("")
        items_list = []
        for child in children:
            row = self.tree.item(child)['values']
            try:
                ratio = float(row[6])
            except:
                ratio = -1.0
            items_list.append((child, ratio))
        sorted_items = sorted(items_list, key=lambda x: x[1], reverse=True)
        for index, (child, _) in enumerate(sorted_items):
            self.tree.move(child, "", index)
        self.append_debug("Main table sorted by Value/AvgPrice in descending order.")

    def show_summary_window(self):
        """
        Computes a summary over all items with valid average prices.
        It sums the item values and the numeric average platinum prices,
        then computes the overall ratio = (total value) / (total platinum cost).
        The summary window displays:
           Total Value, Total Platinum, Overall Value/Plat Ratio.
        """
        total_value = 0
        total_plat = 0
        valid_count = 0
        for child in self.tree.get_children(""):
            row = self.tree.item(child)['values']
            try:
                # Remove any trailing asterisk and convert.
                avg_price = float(str(row[3]).rstrip("*"))
                value = float(row[2])
                total_value += value
                total_plat += avg_price
                valid_count += 1
            except:
                continue
        if valid_count == 0 or total_plat == 0:
            overall_ratio = "N/A"
        else:
            overall_ratio = round(total_value / total_plat, 2)
        summary_window = tk.Toplevel(self.master)
        summary_window.title("Overall Summary")
        frame = tk.Frame(summary_window)
        frame.pack(padx=10, pady=10)
        tk.Label(frame, text=f"Total Value: {total_value}").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(frame, text=f"Total Platinum (Avg Price Sum): {total_plat}").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(frame, text=f"Overall Value/Plat Ratio: {overall_ratio}").grid(row=2, column=0, padx=5, pady=5)
        self.append_debug("Summary window displayed.")

def main():
    root = tk.Tk()
    app = OrderFetcherApp(root)
    root.after(100, app.start_fetching)
    root.mainloop()

if __name__ == "__main__":
    main()
