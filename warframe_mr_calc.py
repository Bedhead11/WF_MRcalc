import requests
import tkinter as tk
from tkinter import ttk
import threading
import time
from datetime import datetime, timezone, timedelta

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

class OrderFetcherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Warframe Market Order Fetcher")
        self.total_items = len(items_data)
        self.current_index = 0

        # Progress UI at the top.
        self.progress_frame = tk.Frame(self.master)
        self.progress_frame.pack(pady=10)
        self.progress_label = tk.Label(self.progress_frame, text="Starting order fetch...")
        self.progress_label.pack(pady=5)
        self.progress_bar = ttk.Progressbar(self.progress_frame, orient="horizontal", length=400, mode="determinate")
        self.progress_bar.pack(pady=5)
        self.progress_bar["maximum"] = self.total_items

        # Main table with columns: Item, Type, Value, Avg Price, Lowest Price, Highest Price, Value/AvgPrice.
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

        # Dictionary to track row IDs so we can update them later.
        self.row_ids = {}
        for item in items_data:
            row_id = self.tree.insert("", "end", values=(item["name"], item["type"], item["value"], "Pending", "Pending", "Pending", "Pending"))
            self.row_ids[item["name"]] = row_id

        # Create a debug window to show full API responses.
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
            # result is expected to be a tuple: (avg_price, lowest, highest)
            if isinstance(result, tuple):
                avg_price, lowest, highest = result
                if isinstance(avg_price, (int, float)) and avg_price != 0:
                    ratio = round(item["value"] / avg_price, 2)
                else:
                    ratio = "N/A"
            else:
                avg_price, lowest, highest, ratio = "N/A", "N/A", "N/A", "N/A"
            # Update row with new values.
            self.master.after(0, self.update_row, name, item["type"], item["value"], avg_price, lowest, highest, ratio)
            self.current_index += 1
            self.master.after(0, self.update_progress, name)
            time.sleep(0.2)
        # After all items are fetched, sort the table by the "Value/AvgPrice" column in descending order.
        self.master.after(0, self.sort_table_by_ratio)

    def fetch_price(self, name):
        """
        For a given item name, fetch orders from the API.
        Filters out orders that lack a platinum value or whose user's last_seen is not within 24 hours.
        Sorts valid orders by platinum (lowest first), then selects the orders ranked 4th–8th.
        Computes and returns a tuple: (average platinum, lowest platinum, highest platinum)
        from those orders. Also outputs debug info.
        """
        try:
            response = requests.get(f"{BASE_URL}/items/{name}/orders")
            debug_response = response.text
            self.master.after(0, self.append_debug, f"Response for {name}:\n{debug_response}\n{'-'*40}")
            if response.ok:
                data = response.json()
                orders = data.get("payload", {}).get("orders", [])
                current_time = datetime.now(timezone.utc)
                valid_orders = []
                for order in orders:
                    if order.get("platinum") is None:
                        continue
                    user = order.get("user", {})
                    last_seen_str = user.get("last_seen")
                    if not last_seen_str:
                        continue
                    try:
                        last_seen_dt = datetime.fromisoformat(last_seen_str)
                    except Exception:
                        continue
                    if (current_time - last_seen_dt) <= timedelta(hours=24):
                        valid_orders.append(order)
                self.master.after(0, self.append_debug, f"For {name}: Found {len(valid_orders)} valid orders.")
                if len(valid_orders) < 4:
                    self.master.after(0, self.append_debug, f"For {name}: Not enough valid orders to compute price.")
                    return "N/A"
                sorted_orders = sorted(valid_orders, key=lambda o: o.get("platinum", float('inf')))
                sorted_platinum = [order.get("platinum") for order in sorted_orders]
                self.master.after(0, self.append_debug, f"For {name}: Sorted platinum values: {sorted_platinum}")
                selected_orders = sorted_orders[3:8]
                selected_platinum = [order.get("platinum") for order in selected_orders]
                self.master.after(0, self.append_debug, f"For {name}: Using platinum values (4th-8th): {selected_platinum}")
                if not selected_orders:
                    return "N/A"
                avg_price = sum(selected_platinum) / len(selected_platinum)
                lowest = min(selected_platinum)
                highest = max(selected_platinum)
                return (round(avg_price, 2), lowest, highest)
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
        """
        Sorts the table rows by the "Value/AvgPrice" column (last column) in descending order.
        Rows with a non-numeric ratio (e.g. "N/A") are treated as -1.
        """
        children = self.tree.get_children("")
        items_list = []
        for child in children:
            row = self.tree.item(child)['values']
            try:
                ratio = float(row[6])
            except:
                ratio = -1.0
            items_list.append((child, ratio))
        # Sort descending by ratio.
        sorted_items = sorted(items_list, key=lambda x: x[1], reverse=True)
        for index, (child, _) in enumerate(sorted_items):
            self.tree.move(child, "", index)
        self.append_debug("Table sorted by Value/AvgPrice in descending order.")

def main():
    root = tk.Tk()
    app = OrderFetcherApp(root)
    root.after(100, app.start_fetching)
    root.mainloop()

if __name__ == "__main__":
    main()
