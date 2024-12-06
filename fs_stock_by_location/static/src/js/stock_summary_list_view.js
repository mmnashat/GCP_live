/** @odoo-module */

import { listView } from "@web/views/list/list_view";
// import { StockSummaryListModel } from "./stock_summary_list_model";
import { StockSummaryListController } from "./stock_summary_list_controller";
import { registry } from "@web/core/registry";

export const StockSummaryListView = {
    ...listView,
    Controller: StockSummaryListController,
    buttonTemplate: 'InventoryAtDate.Buttons',
};

registry.category("views").add('stock_summary_list', StockSummaryListView);
