import React from 'react'

import { useAppDispatch } from '../../hooks/app'
import { sessionFlush } from '../../store/session/utils'
import { sessionOperations } from '../../store/session/operations'

export const LogoutButton: React.FC = () => {
	const dispatch = useAppDispatch()

	const logoutHandler = () => {
		sessionFlush()
		dispatch(sessionOperations.clear())
	}

	return <button onClick={logoutHandler}>Выход</button>
}
