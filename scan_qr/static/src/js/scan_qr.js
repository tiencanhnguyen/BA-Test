odoo.define('scan_qr.scan_qr', function(require) {
    "use strict";

    var KanbanController = require("web.KanbanController");
    var ListController = require("web.ListController");
    var ScanQrDialog = require("scan_qr.ScanQrDialog");

    var scan_qr_dict = {
        custom_events: _.extend({}, ListController.prototype.custom_events,
            KanbanController.prototype.custom_events, {
            search_sale_order: '_onScanQRCode',
        }),
        init: function (parent, model, renderer, params) {
            var self = this;
            this._super.apply(this, arguments);
            this.modelName = params.modelName;
        },
        renderButtons: function () {
            var res = this._super.apply(this, arguments);
            if (this.modelName === "sale.order") {
                this.$buttons.on('click', '.o_scan_qr_button', this._onClickScan.bind(this));
            }
            return res;
        },
        _onClickScan : function() {
            var self = this;
            self.ScanQrDialog = new ScanQrDialog(this).open();
            self.ScanQrDialog.opened();
        },
        _onScanQRCode : function(ev){
            var self = this;
            var data = ev.data;
            self.ScanQrDialog.close()
            self.ScanQrDialog.destroy()
            var filters = self.searchModel.extensions[0][0].state.filters
            var filter_items = Object.values(filters);
            var select_filter = false
            select_filter = filter_items.filter(function (filter) {
                if(filter.fieldName == 'name' && filter.type == 'field'){
                    return filter;
                }
            });
            if(select_filter.length > 0 && data.value){
                const source = self._create_custom_source(select_filter, data.value)
                if (source){
                    self.searchModel.dispatch('addAutoCompletionValues', {
                        filterId: source.filterId,
                        value: source.label,
                        label: source.label,
                        operator: source.filterOperator || source.operator,
                    });
                }
            }
        },
        _create_custom_source: function(select_filter, value){
            if(select_filter){
                return {
                    active: true,
                    label:value,
                    description: select_filter[0].description,
                    filterId: select_filter[0].id,
                    filterOperator: select_filter[0].operator,
                    id: 1,
                    operator: 'ilike',
                    parent: false,
                    type:'char',
                };
            }
        }
    };

    KanbanController.include(scan_qr_dict);
    ListController.include(scan_qr_dict);
});
