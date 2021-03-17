odoo.define('scan_qr.ScanQrDialog', function(require) {
    "use strict";

    var Dialog = require('web.Dialog');
    var core = require('web.core');
    var _t = core._t;

    var ScanQrDialog = Dialog.extend({
        template: "ScanQrDialog",
        jsLibs: ['scan_qr/static/lib/html5-qrcode.min.js'],
        init: function (parent, options) {
            options = options || {};
            this.html5QrCode = false;
            options.title = options.title || _t("Scan QR code");
            options.size = options.size || 'medium';

            if (!options.buttons) {
                options.buttons = [];
                options.buttons.push({text: _t("Cancel"), close: true});
            }
            this._super(parent, options);
        },
        opened: function(){
            var self = this;
            this._super.apply(this, arguments).then(function(){
                const config = { fps: 10, qrbox: 250};
                self.html5QrCode = new Html5Qrcode('reader');
                const qrCodeSuccessCallback = message => {
                    self.trigger_up('search_sale_order', { value: message });
                };
                const qrCodeErrorCallback = message => {
                    return;
                }
                self.html5QrCode.start({ facingMode: "environment" }, config, qrCodeSuccessCallback.bind(self), qrCodeErrorCallback.bind(self));
            });
        },
        
        close: function () {
            var self = this;
            self.html5QrCode.stop();
            this._super.apply(this, arguments);
        },
    });
    return ScanQrDialog;
});
