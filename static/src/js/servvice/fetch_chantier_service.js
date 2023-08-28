/** @odoo-module */

import { registry } from "@web/core/registry"

export const chantierListService = {
    dependencies:["orm", "user", "rpc","notification"],
    async start(env, { orm, user, rpc, notification }){

        async function fetchChantierList(){
            const ids = []
            await orm.searchRead("chantier.responsable.relation", [('user_id','=',user.userId)], ['chantier_id']).then((result) => {
                result.forEach( element => {
                    ids.append(element.chantier_id)
                });
                
            })
            return await orm.searchRead("fleet.vehicle.chantier", [('id','in',ids)], ['code','name'])
        }
    
        return {
            chantierlist:fetchChantierList()
        }
    }
}

registry.category('services').add("chantierListService", chantierListService)