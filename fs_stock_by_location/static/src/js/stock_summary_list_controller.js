/** @odoo-module */

import { useBus } from "@web/core/utils/hooks";
import { session } from "@web/session";
import { ListController } from "@web/views/list/list_controller";

export class StockSummaryListController extends ListController {
    async onClickFSInventoryAtDate() {
        const context = {
            active_model: this.props.resModel,
        };
        this.actionService.doAction({
            res_model: "stock.summary.generate",
            views: [[false, "form"]],
            target: "new",
            type: "ir.actions.act_window",
            context,
        });
    }
}
