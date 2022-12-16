import { TUserResponse } from '../types/user'

export const userAPI = {
	getUser: () => {
		return new Promise<TUserResponse>((resolve) =>
			setTimeout(
				() =>
					resolve({
						first_name: 'Никита',
						last_name: 'Нельсон',
						email: 'nikitazharov2',
						current_word_id: 1,
						attempts: [],
					}),
				500
			)
		)
	},
	getUserBad: () => {
		return new Promise((resolve, reject) => {
			reject(new Error("Request failed, bombasticn't API"))
		})
	},
}
