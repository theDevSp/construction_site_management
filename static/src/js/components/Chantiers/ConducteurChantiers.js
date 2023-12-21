/** @odoo-module */

import { loadCSS, loadJS } from "@web/core/assets";
const { Component, onMounted, onWillStart } = owl;
import { useService } from "@web/core/utils/hooks"

export class ConducteurChantiers extends Component {
    setup() {
        this.rpc = useService("rpc");

        onMounted(async () => {
            this.mountInputs()
        })
    }

    async mountInputs() {

        const props = this.props
        this.allChantiers = await this.rpc(`/hr_management/users/get_all_chantiers`);

        if (this.allChantiers && this.allChantiers.data && this.allChantiers.data.length > 0) {
            const firstID = this.allChantiers.data[0].id;
            $('#select-chantier').selectize({
                maxItems: 1,
                minItems: 1,
                valueField: 'id',
                labelField: 'name',
                searchField: 'name',
                options: this.allChantiers.data,
                create: false,
                items: [firstID],
                onInitialize: function () {
                    props.onChangeChantier(this.getValue());
                },
                onChange: function (value) {
                    props.onChangeChantier(value);
                }
            });

        } else {
            window.location.href = '/';
        }

    }


}

ConducteurChantiers.template = "owl.ConducteurChantiers"